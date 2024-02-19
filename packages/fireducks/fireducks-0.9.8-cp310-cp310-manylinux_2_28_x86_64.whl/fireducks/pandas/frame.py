# Copyright (c) 2023 NEC Corporation. All Rights Reserved.
"""FireDucks: Dataframe with FIRE
"""
from __future__ import annotations

from firefw import tracing

import logging
import os
import warnings

import numpy as np

with tracing.scope(tracing.Level.DEFAULT, "import pandas"):
    import pandas
    from pandas.util._decorators import deprecate_nonkeyword_arguments
    from pandas.util._validators import validate_bool_kwarg
    import pandas.api.extensions as pandas_extensions
    from pandas._libs.lib import is_all_arraylike

import fireducks.core
from fireducks import ir, irutils
from fireducks.pandas.binop import (
    # get_binop_vector_scalar,
    # get_binop_vector_vector,
    get_binop_table_scalar,
    get_binop_table_vector,
    get_binop_table_table,
)

import fireducks.pandas.utils as utils
from fireducks.pandas.utils import (
    _unwrap,
    make_agg_args,
    is_supported_df_agg_funcs,
)

from fireducks.pandas.generic import (
    FireDucksPandasCompat,
    _Scalar,
    _install_binops,
    _install_fallback_mutating_method,
    _install_unary_op_fallbacks,
    _wrap_pandas,
)

from fireducks.pandas.series import Series
from fireducks.pandas.wrappers import Index, MultiIndex, DatetimeIndex
from fireducks.pandas.expr import QueryParser
from fireducks.pandas.metadata import IRMetadataWrapper

logger = logging.getLogger(__name__)


def _setup_DataFrame(cls):
    utils.install_fallbacks(cls, ["__contains__"])
    _install_unary_op_fallbacks(cls, pandas.DataFrame)
    _install_binops(cls, pandas.DataFrame)

    # `_set_value` is used to call _fallback_mutating_method in
    # `test_anti_dep_fallback`. If you change it to non-fallback, please fix
    # the test. See GT #1069
    _install_fallback_mutating_method(cls, "_set_value")
    _install_fallback_mutating_method(cls, "__delitem__")

    _wrap_pandas(cls, pandas.DataFrame)
    return cls


def create_metadata(df: pandas.DataFrame):
    """Create IR metadata to pass to from_pandas"""
    from fireducks.fireducks_ext import (
        Metadata,
        ColumnMetadata,
        Scalar,
        ColumnName,
    )

    index = df.columns
    logger.debug("create_metadata: df.columns.nlevels=%d", index.nlevels)
    logger.debug("create_metadata: df.columns.names=%s", index.names)
    logger.debug(
        "create_metadata: isMultiindex=%s",
        isinstance(index, pandas.MultiIndex),
    )

    def to_column_name(name, isMulti):
        if isinstance(name, (frozenset, tuple)):
            if isMulti:
                return ColumnName.Multi([Scalar(e) for e in name])
            else:
                return ColumnName.SingleFromScalars([Scalar(e) for e in name])
        else:
            # return [Scalar(name)]
            return ColumnName.Single(Scalar(name))

    isMulti = isinstance(index, pandas.MultiIndex)
    column_names = [to_column_name(name, isMulti) for name in index]
    columns = [ColumnMetadata(name) for name in column_names]
    column_index_names = [Scalar(name) for name in index.names]
    return Metadata(
        columns, column_index_names, isinstance(df.index, pandas.MultiIndex)
    )


def _from_pandas_frame(df: pandas.DataFrame):
    """
    Returns fire.Value
    """
    logger.debug("_from_pandas_frame")
    if fireducks.core.get_ir_prop().has_metadata:
        # rename to ensure no duplicated column name. Here we will rename only
        # columns, but those should not conflict with index. We use
        # `__fireducks_dummy_` prefix.
        copy = df.copy(deep=False)
        copy.columns = [
            f"__fireducks_dummy_{i}" for i in range(len(df.columns))
        ]
        f = fireducks.core.make_available_value(copy, ir.Ty_pyobj)
        metadata = create_metadata(df)
        # logger.debug('_from_pandas_frame: metadata=%s', metadata)
        m = fireducks.core.make_available_value(metadata, ir.Ty_metadata)
        return ir.from_pandas_frame_metadata(f, m)
    else:
        f = fireducks.core.make_available_value(df, ir.Ty_pyobj)
        return ir.from_pandas_dataframe(f)


def _is_columns_dict(obj):
    if not isinstance(obj, dict):
        return False

    return all([irutils.is_column_name(x) for x in obj.keys()]) and all(
        [isinstance(x, Series) for x in obj.values()]
    )


def _parse_frame_creation_args(args, kwargs):
    value = kwargs.get("_value")

    if value is not None:
        return value, None

    if len(kwargs) == 0 and len(args) == 1 and _is_columns_dict(args[0]):
        value = ir.create_table_from_columns(
            columns=irutils.make_tuple_of_tables(args[0].values()),
            column_names=irutils.make_tuple_of_column_names(args[0].keys()),
        )
        return value, None

    obj = kwargs.pop("__fireducks_from_pandas", None)
    if obj is None:
        reason = "args of DataFrame.__init__"
        tmp = [_unwrap(x, reason=reason) for x in args]
        obj = pandas.DataFrame(*tmp, **_unwrap(kwargs))
    assert isinstance(obj, pandas.DataFrame)

    return _from_pandas_frame(obj), obj


@_setup_DataFrame
class DataFrame(FireDucksPandasCompat):
    _constructor_sliced: type[Series] = Series
    _metadata = []

    def __init__(self, *args, **kwargs):
        """
        Three types of constructors.

        1. Construct from fire.Value
             Used when kwargs has `_value`
        2. Construct from pandas.DataFrame
             Used when kwargs has `__fireducks_from_pandas`
        3. Construct from pandas-like arguments
             Used in other cases
        """
        logger.debug("DataFrame.__init__")

        value, obj = _parse_frame_creation_args(args, kwargs)
        super().__init__(value, pandas_object=obj)

        if fireducks.core.get_fireducks_options().benchmark_mode:
            self._evaluate()

    def __dir__(self):
        reason = "DataFrame.__dir__ is called"
        return self._fallback_call("__dir__", __fireducks_reason=reason)

    def __finalize__(self, other, method=None):
        logger.debug("DataFrame.__finalize__: method=%s", method)
        if isinstance(other, DataFrame):
            for name in set(self._metadata) & set(other._metadata):
                assert isinstance(name, str)
                logger.debug("DataFrame.__finalize__: setattr name=%s", name)
                object.__setattr__(self, name, getattr(other, name, None))
        return self

    def __getattr__(self, name):
        logger.debug("DataFrame.__getattr__: name=%s", name)

        # avoiding unnecessary fallback for methods which might be called
        # from utilities like ipython display formatters...
        ipy_unsupp = [
            "_ipython_display_",
            "_ipython_canary_method_should_not_exist_",
        ]
        repr_unsupp = [
            "pretty",
            "svg",
            "png",
            "jpeg",
            "javascript",
            "markdown",
            "mimebundle",
            "pdf",
            "json",
        ]
        if name in ipy_unsupp + ["_repr_" + x + "_" for x in repr_unsupp]:
            return object.__getattribute__(self, name)

        # Because fireducks.DataFrame do not explicitly define all
        # pandas.DataFrame API, undefined API reaches here when it is called.
        # It should be handled as API, not as column name, we have to check if
        # it is API.
        if name not in pandas.DataFrame.__dict__:
            if self._is_column_name(name):
                return self[name]

        reason = f"{type(self).__name__}.__getattr__ for {name} is called"
        return utils.fallback_attr(self._unwrap, name, reason)

    def __len__(self):
        return self.shape[0]

    def __iter__(self):
        return iter(self._get_column_names())

    def __abs__(self):
        return self.abs()

    def __neg__(self):
        return DataFrame._create(ir.negate(self._value))

    def __round__(self, decimals=0):
        return self.round(decimals)

    def __repr__(self):
        ret, is_trunc = self.__get_trunc_repr_method_result__(
            method="__repr__"
        )
        if is_trunc:
            truncated_shape_info = ret.rsplit("\n", 1)[1]
            nrow, ncol = self.shape  # actual
            actual_shape_info = (
                "[" + str(nrow) + " rows x " + str(ncol) + " columns]"
            )
            # replacing truncated shape info with actual shape info
            truncated_shape_info_len = len(truncated_shape_info)
            return ret[:-truncated_shape_info_len] + actual_shape_info
        else:
            return ret

    def _repr_html_(self):
        ret, is_trunc = self.__get_trunc_repr_method_result__(
            method="_repr_html_"
        )
        if is_trunc:
            truncated_shape_info = "\n".join(ret.rsplit("\n", 2)[1:])
            nrow, ncol = self.shape  # actual
            actual_shape_info = (
                "<p>"
                + str(nrow)
                + " rows x "
                + str(ncol)
                + " columns</p>\n</div>"
            )
            # replacing truncated shape info with actual shape info
            truncated_shape_info_len = len(truncated_shape_info)
            return ret[:-truncated_shape_info_len] + actual_shape_info
        else:
            return ret

    def _repr_latex_(self):
        if self._fireducks_meta.is_cached():
            return utils._wrap(self._fireducks_meta.get_cache()._repr_latex_())

        # to avoid fallback...
        if not pandas.get_option("display.latex.repr"):
            return None

        reason = f"{type(self).__name__}._repr_latex_ is called"
        return utils.fallback_attr(self._unwrap, "_repr_latex_", reason)

    def __invert__(self):
        return DataFrame._create(ir.invert(self._value))

    def __setattr__(self, name, value):
        logger.debug("DataFrame.__setattr__: name=%s", name)

        # Known fireducks.DataFrame properties
        # Because columns is property, __setattr__ is called when columns = ..
        if name in ["_value", "columns", "index"]:
            return object.__setattr__(self, name, value)

        if name in ["attrs"]:
            return self._fallback_mutating_method(
                "__setattr__", args=[name, value]
            )

        # Existing user-defined properties
        try:
            object.__getattribute__(self, name)
            return object.__setattr__(self, name, value)
        except AttributeError:
            pass

        if name in self.columns:
            return self.__setitem__(name, value)

        # New user-defined properties
        object.__setattr__(self, name, value)

    @classmethod
    def _create(cls, value):
        assert value.type() == ir.TableType
        return DataFrame(_value=value)

    def _create_or_inplace(self, value, inplace):
        inplace = validate_bool_kwarg(inplace, "inplace")
        if inplace:
            return self._rebind(value, invalidate_cache=True)
        return DataFrame._create(value).__finalize__(self)

    @classmethod
    def _get_axis_number(cls, axis):
        return pandas.DataFrame._get_axis_number(axis)

    def _get_column_names(self):
        # To prevent fallback, cache is explicitly checked here
        if self._fireducks_meta.is_cached():
            return list(self._fireducks_meta.get_cache().columns)
        else:
            if fireducks.core.get_ir_prop().has_metadata:
                return self._get_metadata().column_names
            return list(self.columns)

    def _is_column_name(self, name):
        return name in self._get_column_names()

    # fireducks method for debug
    def _print(self):
        ch = ir.print_table(self._value)
        fireducks.core.evaluate([ch])

    # def _build_row_func(self, func) -> fire.Value:
    #     return fire.make_available_value(func, ir.Ty_pyobj)

    def _to_pandas(self, options=None):
        if fireducks.core.get_ir_prop().has_metadata:
            result = _to_pandas_frame_metadata(self._value, options)
        else:
            value = ir.to_pandas(self._value)
            result = fireducks.core.evaluate([value], options)[0]
        assert isinstance(
            result, pandas.DataFrame
        ), f"{type(result)} is not pandas.DataFrame"

        return result

    @classmethod
    def from_pandas(cls, df):
        if not isinstance(df, pandas.DataFrame):
            raise RuntimeError(
                "DataFrame.from_pandas: illegal argument: "
                f"{df.__class__.__name__}"
            )
        return DataFrame(__fireducks_from_pandas=df)

    #
    # Pandas methods (alphabetical)
    #

    # fireducks.DataFrame.__getitem__ returns Series even when DataFrame has
    # multilevel column index. This method can force returning DataFrame.
    def _project(self, key, as_frame=False):
        cls = Series
        if as_frame or isinstance(key, list):
            cls = DataFrame

        if isinstance(key, list):
            key = irutils.make_vector_or_scalar_of_column_name(key)
            return cls._create(ir.project(self._value, key)).__finalize__(
                self, method="project"
            )

        key = irutils.make_vector_or_scalar_of_column_name(key)
        return cls._create(ir.project(self._value, key))

    def __getitem__(self, key):
        logger.debug("DataFrame.__getitem__: type(key)=%s", type(key))
        if isinstance(key, Series):
            dtype = utils._deduce_dtype(key)
            if dtype is not None and dtype == bool:
                return DataFrame._create(ir.filter(self._value, key._value))
            return self._fallback_call("__getitem__", _unwrap(key))

        elif isinstance(key, slice) and utils.is_int_or_none_slice(key):
            if key.step is None or key.step == 1:
                return self._slice(key)

        if isinstance(key, Index):
            key = list(key)
        if irutils.is_column_name(key) or (
            isinstance(key, list)
            and all([irutils.is_column_name(x) for x in key])
        ):
            return self._project(key)

        reason = f"Unsupported key type: {type(key)}"
        return self._fallback_call(
            "__getitem__", key, __fireducks_reason=reason
        )

    def __setitem__(self, key: str, value):
        logger.debug("DataFrame.__setitem__")

        def _fallback(key=key, value=value, reason=None):
            self._fallback_mutating_method(
                "__setitem__",
                args=[_unwrap(key, reason="unwrap key of __setitem__"), value],
                reason=reason,
            )

        if not (isinstance(key, str) or utils._is_str_list_or_index(key)):
            return _fallback(reason="key is neither str nor list of str")

        if irutils.irable_scalar(value):
            key = irutils.make_vector_or_scalar_of_column_name(key)
            value = irutils.make_vector_or_scalar_of_scalar(value)
            self._rebind(
                ir.assign_scalar(self._value, key, value),
                invalidate_cache=True,
            )
            return self

        from_list = False
        from_ndarray = False
        if isinstance(value, list):
            # See GT #1864
            unwrap_not_required = all(
                [isinstance(x, (int, float, str)) for x in value]
            )
            if unwrap_not_required:
                # To bypass unwrap in Series.__init__, create pandas.Series.
                value = Series.from_pandas(pandas.Series(value))
                from_list = True

        if isinstance(value, np.ndarray) and value.ndim == 1:
            value = Series(value)
            from_ndarray = True

        if isinstance(value, (Index, range)):
            value = Series(value)
            from_ndarray = True  # just to perform size check at backend

        if not isinstance(value, FireDucksPandasCompat):
            return _fallback(reason="value is not FireDucksPandasCompat")

        if isinstance(key, Index):
            key = list(key)
        keys = irutils.make_vector_or_scalar_of_str(key)
        self._rebind(
            ir.setitem(
                self._value, keys, value._value, from_list, from_ndarray
            ),
            invalidate_cache=True,
        )
        return self

    def abs(self):
        return DataFrame._create(ir.abs(self._value))

    def aggregate(self, func=None, axis=0, *args, **kwargs):
        axis = self._get_axis_number(axis)
        reason = None

        if irutils._is_scalar_or_list_or_tuple_of(func, str):
            targets = [func] if isinstance(func, str) else func
            if axis == 1:
                supported_func_on_axis_1 = ["sum", "all", "any"]
                if any([f not in supported_func_on_axis_1 for f in targets]):
                    reason = (
                        f"unsupported aggregate function: {func} on axis=1"
                    )
            else:
                if not is_supported_df_agg_funcs(targets):
                    reason = (
                        f"unsupported aggregate function: {func} on axis=0"
                    )
            if not reason:
                funcs = irutils.make_vector_or_scalar_of_str(func)
                value = ir.aggregate(self._value, funcs, axis)
                if isinstance(func, str):  # scalar
                    return Series._create(value)
                return DataFrame._create(value)

        if axis == 1:  # not supported for dict, args, kwargs cases
            reason = "unsupported aggregated args on axis=1"
        else:
            aggArgs = make_agg_args(func, *args, **kwargs)
            if aggArgs is None:
                reason = "unsupported aggregated args"

        if not reason:
            if not is_supported_df_agg_funcs(aggArgs.funcs):
                reason = (
                    "all or few agg functions are not supported"
                    f" {aggArgs.funcs}"
                )

        if reason is not None:
            return self._fallback_call(
                "aggregate",
                func,
                axis,
                *args,
                **kwargs,
                __fireducks_reason=reason,
            )

        funcs, columns, relabels = aggArgs.to_ir()
        value = ir.aggregate_specified(
            self._value, funcs, columns, relabels, axis
        )

        if not kwargs and all(
            [isinstance(func, str) for func in aggArgs.funcs]
        ):
            return Series._create(value)  # Series when all funcs are scalar
        return DataFrame._create(value)

    agg = aggregate

    def apply(self, func, axis=0, **kwargs):
        if callable(func):

            def wrapper(*args, **kwargs):
                # Because func will be called by pandas, args and kwargs might
                # be pandas's object. func might use fireducks's data or func
                # itself is fireducks's function, args and kwargs should be
                # converted to ducks's one.
                args = utils._wrap(args)
                kwargs = utils._wrap(kwargs)
                return _unwrap(func(*args, **kwargs))

            return self._fallback_call("apply", wrapper, axis, **kwargs)
        else:
            return self._fallback_call("apply", func, axis, **kwargs)
        # pandas.DataFrame.apply(func) returns a DataFrame instead of a Series
        # depending on the return value of func.
        #
        # if axis != 1:
        #   logger.warn(
        #       'fireducks.DataFrame.apply is currently only supported'
        #       ' if axis is 1')
        # assert callable(func)
        # func = self._build_row_func(func)
        # return Series._create(ir.apply_row(self._value, func))

    def assign(self, **kwargs):
        data = self.copy()
        for k, v in kwargs.items():
            data[k] = v(data) if callable(v) else v
        return data

    def _set_column_index_names(self, names):  # inplace
        logger.debug("DataFrame._set_column_index_names")
        names = irutils.make_tuple_of_scalars(names)
        value = ir.set_column_index_names(self._value, names)
        self._rebind(value, invalidate_cache=True)

    @property
    def columns(self):
        """The column labels of the DataFrame."""
        logger.debug("DataFrame.columns")
        if self._fireducks_meta.is_cached():
            columns = utils._wrap(self._fireducks_meta.get_cache().columns)
            columns._set_fireducks_frame(self, "columns")
            return columns

        if fireducks.core.get_ir_prop().has_metadata:
            metadata = self._get_metadata()
            pandas_columns = metadata.create_column_index()
            columns = utils._wrap(pandas_columns)
            columns._set_fireducks_frame(self, "columns")
            return columns

        columns = utils.fallback_attr(
            self._unwrap,
            "columns",
            reason=f"{type(self).__name__}.columns",
        )
        columns._set_fireducks_frame(self, "columns")
        return columns

    @columns.setter
    def columns(self, value):
        logger.debug("columns: type=%s", type(value))
        if value is None:
            raise TypeError(
                "Index(...) must be called with a collection of some kind"
                ", None was passed"
            )
        if not irutils._is_irable_scalar_arraylike(value):
            return self._fallback_mutating_method(
                "__setattr__",
                args=["columns", value],
                reason="columns_setter: input is not an array-like of irable-scalar",
            )
        cols = irutils.make_tuple_of_scalars(value)
        self._rebind(ir.rename(self._value, cols), invalidate_cache=True)
        return self

    def corr(self, *args, **kwargs):
        decoded = utils.decode_args(args, kwargs, pandas.DataFrame.corr)
        if decoded.numeric_only is pandas_extensions.no_default:
            decoded.numeric_only = True
        decoded.numeric_only = validate_bool_kwarg(
            decoded.numeric_only, "numeric_only"
        )
        reason = []

        supported_methods = ["pearson"]
        if isinstance(decoded.method, str):
            if decoded.method not in supported_methods:
                reason.append(f"unsupported method={decoded.method}")
        else:
            reason.append(
                "unsupported 'method' of type ="
                f"'{type(decoded.method).__name__}'"
            )

        if decoded.min_periods is None:
            decoded.min_periods = 1
        elif not isinstance(decoded.min_periods, int):
            reason.append(f"unsupported min_periods={decoded.min_periods}")

        decoded.min_periods = max(0, decoded.min_periods)

        if len(reason) > 0:
            return self._fallback_call_packed(
                "corr",
                args,
                kwargs,
                reason="; ".join(reason),
            )

        return DataFrame._create(
            ir.table_corr(
                self._value,
                decoded.method,
                decoded.min_periods,
                decoded.numeric_only,
            )
        )

    def diff(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.diff)
        if arg.axis == 0 or arg.axis == "index":
            if not isinstance(arg.periods, int):
                reason = "periods is not int"
            else:
                return DataFrame._create(ir.diff(self._value, arg.periods))
        else:
            reason = "unsupported argument"

        return self._fallback_call(
            "diff", *args, **kwargs, __fireducks_reason=reason
        )

    @deprecate_nonkeyword_arguments(
        version=None, allowed_args=["self", "labels"]
    )
    def drop(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.drop)
        arg.inplace = validate_bool_kwarg(arg.inplace, "inplace")

        if arg.labels is not None:
            if arg.index is not None or arg.columns is not None:
                raise ValueError(
                    "Cannot specify both 'labels' and 'index'/'columns'"
                )
            if arg.axis == 1:
                arg.columns = arg.labels
            else:
                arg.index = arg.labels
        elif arg.index is None and arg.columns is None:
            raise ValueError(
                "Need to specify at least one of "
                "'labels', 'index' or 'columns'"
            )
        reason = arg.is_not_default(["level", "errors"])

        output = None
        if reason is None:
            if arg.columns is not None:
                if isinstance(arg.columns, str):
                    arg.columns = [arg.columns]
                if utils._is_str_list_or_index(arg.columns):
                    arg.columns = irutils.make_tuple_of_column_names(
                        arg.columns
                    )
                    value = ir.drop_columns(self._value, arg.columns)
                    output = self._create_or_inplace(value, arg.inplace)
                else:
                    reason = "columns is not a list or Index of str"

        if reason is None:
            if arg.index is not None:
                if irutils.irable_scalar(arg.index):
                    arg.index = Index([arg.index])
                if isinstance(arg.index, list):
                    if np.all([irutils.irable_scalar(i) for i in arg.index]):
                        arg.index = Index(arg.index)
                    elif np.all([isinstance(i, tuple) for i in arg.index]):
                        arg.index = MultiIndex.from_tuples(arg.index)
                if isinstance(arg.index, (Index, MultiIndex)):
                    indices = DataFrame(index=arg.index)
                    tbl = self if output is None else output
                    output = tbl._create_or_inplace(
                        ir.drop_rows(tbl._value, indices._value), arg.inplace
                    )
                else:
                    reason = "index is not a scalar, list or Index "

        if reason is None:
            return output

        return self._fallback_may_inplace(
            "drop", args, kwargs, pos=5, reason=reason
        )

    def drop_duplicates(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.drop_duplicates)
        arg.inplace = validate_bool_kwarg(arg.inplace, "inplace")
        arg.ignore_index = validate_bool_kwarg(
            arg.ignore_index, "ignore_index"
        )
        supported_keep = {"first", "last", False}

        if (
            (
                arg.subset is None
                or isinstance(arg.subset, str)
                or (
                    utils._is_str_list_or_index(arg.subset)
                    and len(arg.subset) > 0
                )
            )
            and arg.keep in supported_keep
            and not arg.inplace
            and not arg.ignore_index
        ):
            if arg.subset is None:
                arg.subset = []  # empty means all column
            if isinstance(arg.subset, str):
                arg.subset = [arg.subset]
            logger.debug(f"subset.size={len(arg.subset)}")
            arg.subset = irutils.make_tuple_of_column_names(arg.subset)
            arg.keep = "none" if not arg.keep else arg.keep
            return DataFrame._create(
                ir.drop_duplicates(self._value, arg.subset, arg.keep)
            )

        return self._fallback_may_inplace(
            "drop_duplicates",
            args,
            kwargs,
            pos=3,
            reason="unsupported argument",
        )

    def dropna(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.dropna)
        if arg.axis == 0 or arg.axis == "index":
            if (
                arg.subset is None
                or isinstance(arg.subset, str)
                or (
                    utils._is_str_list_or_index(arg.subset)
                    and len(arg.subset) > 0
                )
            ):
                if arg.subset is None:
                    arg.subset = []  # empty means all column
                if isinstance(arg.subset, str):
                    arg.subset = [arg.subset]
                logger.debug(f"subset.size={len(arg.subset)}")
                subset = irutils.make_tuple_of_column_names(arg.subset)

                if arg.thresh is pandas_extensions.no_default:
                    if (
                        arg.how is pandas_extensions.no_default
                        or arg.how == "any"
                    ):
                        value = ir.dropna(self._value, subset, True, 0)
                        return self._create_or_inplace(value, arg.inplace)
                    elif arg.how == "all":
                        value = ir.dropna(self._value, subset, False, 1)
                        return self._create_or_inplace(value, arg.inplace)

                else:
                    if arg.how is pandas_extensions.no_default:
                        value = ir.dropna(
                            self._value, subset, False, arg.thresh
                        )
                        return self._create_or_inplace(value, arg.inplace)

        return self._fallback_may_inplace(
            "dropna",
            args,
            kwargs,
            pos=3,
            reason="unsupported argument",
        )

    def duplicated(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.duplicated)
        supported_keep = {"first", "last", False}

        if (
            arg.subset is None
            or isinstance(arg.subset, str)
            or (
                utils._is_str_list_or_index(arg.subset) and len(arg.subset) > 0
            )
        ) and arg.keep in supported_keep:
            if arg.subset is None:
                arg.subset = []  # empty means all column
            if isinstance(arg.subset, str):
                arg.subset = [arg.subset]
            logger.debug(f"subset.size={len(arg.subset)}")
            arg.subset = irutils.make_tuple_of_column_names(arg.subset)
            arg.keep = "none" if not arg.keep else arg.keep
            return Series._create(
                ir.duplicated(self._value, arg.subset, arg.keep)
            )

        return self._fallback_call(
            "duplicated",
            arg.subset,
            arg.keep,
            __fireducks_reason="unsupported argument",
        )

    @property
    def dtypes(self):
        # This method returns PandasWrapper, not fireducks.Series because
        # contents of Series is numpy.dtype, i.e. python object, which can not
        # be converted to arrow.

        def wrap(obj):
            return utils.PandasWrapper(obj, Series)

        if self._fireducks_meta.is_cached():
            return wrap(self._fireducks_meta.get_cache().dtypes)

        if fireducks.core.get_ir_prop().has_metadata:
            dtypes, unsupported = self._get_metadata().dtypes
            if len(unsupported) == 0:
                return wrap(dtypes)
            reason = "DataFrame.dtypes includes unsupported type: " + ",".join(
                unsupported
            )
        else:
            reason = "IR does not support metadata"

        return utils.fallback_attr(
            self._unwrap, "dtypes", reason=reason, wrap_func=wrap
        )

    def explode(self, column, ignore_index=False):
        if isinstance(column, list):
            if not column:
                raise ValueError("column must be nonempty")
            is_supported_names = all(
                [irutils.is_column_name(x) for x in column]
            )
            if is_supported_names and len(column) > len(set(column)):
                raise ValueError("column must be unique")
        else:
            is_supported_names = irutils.is_column_name(column)

        if not is_supported_names:
            reason = f"unsupported column of type: {type(column).__name__}"
            return self._fallback_call(
                "explode", column, ignore_index, __fireducks_reason=reason
            )

        column = [column] if not isinstance(column, list) else column
        column = irutils.make_tuple_of_column_names(column)
        # according to pandas behavior. all true values would be treated
        # as true. e.g., ignore_index="a" would be treated as ignore_index=True
        ignore_index = bool(ignore_index)
        return DataFrame._create(ir.explode(self._value, column, ignore_index))

    def eval(self, *args, **kwargs):
        kwargs["level"] = kwargs.pop("level", 0) + 5
        return self._fallback_call("eval", *args, **kwargs)

    def filter(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.filter)
        if arg.axis is None:
            arg.axis = 1

        reason = arg.is_not_default(["like", "regex"])
        if reason:
            pass
        elif not irutils._is_scalar_or_list_or_tuple_of(arg.items, str):
            reason = "items is not a list of str"
        elif not (arg.axis == 1 or arg.axis == "columns"):
            reason = "axis is not 1"
        else:
            labels = self._get_column_names()
            cols = [r for r in arg.items if r in labels]
            return self[cols]

        return self._fallback_call(
            "filter", *args, **kwargs, __fireducks_reason=reason
        )

    def groupby(self, by=None, *args, **kwargs):
        logger.debug("groupby: type(by)=%s", type(by))
        from fireducks.pandas.groupby import DataFrameGroupBy

        return DataFrameGroupBy(self, by=by, *args, **kwargs)

    def insert(self, *args, **kwargs):
        # TODO: unwrap args when it includes fireducks.pandas.Series
        self._fallback_mutating_method("insert", args, kwargs)

    def isna(self):
        return DataFrame._create(ir.isnull(self._value))

    def isnull(self):
        return DataFrame._create(ir.isnull(self._value))

    def join(self, *args, **kwargs):
        class MergeOperation:
            def __init__(self, left, right):
                self.left = left
                self.right = right

        arg = utils.decode_args(args, kwargs, pandas.DataFrame.join)
        if not isinstance(arg.other, DataFrame):
            reason = "other is not DataFrame"
        elif arg.how not in ("left", "right", "inner", "outer"):
            reason = "how is not left, right, inner, or outer"
        elif not isinstance(arg.lsuffix, str):
            reason = "lsuffix is not str"
        elif not isinstance(arg.rsuffix, str):
            reason = "rsuffix is not str"
        else:
            reason = arg.is_not_default(
                [
                    "on",
                    # "how", "lsuffix", "rsuffix",
                    "sort",
                    "validate",
                ]
            )

        if reason:
            return self._fallback_call_packed(
                "join", args, kwargs, reason=reason
            )

        op = MergeOperation(self, arg.other)
        on = irutils.make_tuple_of_column_names([])
        left_on = right_on = on
        return DataFrame._create(
            ir.join(
                self._value,
                arg.other._value,
                arg.how,
                on,
                left_on,
                True,
                right_on,
                True,
                arg.lsuffix,
                arg.rsuffix,
            )
        ).__finalize__(op, "merge")

    def melt(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.melt)
        reason = arg.is_not_default(["col_level"])
        if reason is not None:
            return self._fallback_call(
                "melt", *args, **kwargs, __fireducks_reason=reason
            )

        arg.id_vars = irutils.make_vector_or_scalar_of_column_name(arg.id_vars)
        arg.value_vars = irutils.make_vector_or_scalar_of_column_name(
            arg.value_vars
        )
        arg.var_name = irutils.make_column_name(arg.var_name)
        arg.value_name = irutils.make_column_name(arg.value_name)
        value = ir.melt(
            self._value,
            arg.id_vars,
            arg.value_vars,
            arg.var_name,
            arg.value_name,
            arg.ignore_index,
        )
        return DataFrame._create(value)

    def items(self):
        df = self.to_pandas()
        for label, column in df.items():
            yield label, utils._wrap(column)

    def mask(self, cond, *args, **kwargs):
        if callable(cond):
            cond = cond(self)

        if not hasattr(cond, "__invert__"):
            cond = np.array(cond)

        return self.where(~cond, *args, **kwargs)

    def merge(
        self,
        *args,
        **kwargs,
    ):
        class MergeOperation:
            def __init__(self, left, right):
                self.left = left
                self.right = right

        arg = utils.decode_args(args, kwargs, pandas.DataFrame.merge)
        reason = None
        if not (
            isinstance(arg.suffixes, (list, tuple))
            and len(arg.suffixes) == 2
            and all([isinstance(x, (str, type(None))) for x in arg.suffixes])
        ):
            reason = "unsupported suffix"
        elif not isinstance(arg.left_index, bool) or not isinstance(
            arg.right_index, bool
        ):
            reason = "left_index or right_index is not bool"
        elif not irutils.is_column_name_or_column_names(arg.left_on):
            reason = "left_on is not column name supported by IR"
        elif not irutils.is_column_name_or_column_names(arg.right_on):
            reason = "right_on is not column name supported by IR"
        elif arg.how not in ("left", "right", "inner", "outer"):
            reason = f"unsupported how: {arg.how}"
        else:
            reason = arg.is_not_default(
                ["sort", "copy", "indicator", "validate"]
            )

        op = MergeOperation(self, arg.right)

        if reason is not None:
            return self._fallback_call_packed(
                "merge", args, kwargs, reason=reason
            ).__finalize__(op, "merge")

        left_suffix, right_suffix = [
            # Replace None with "\0" so that IR can recognize the
            # difference between None and ""(empty string).
            s if s is not None else chr(0)
            for s in arg.suffixes
        ]

        # None cannot be used as column name in merge, so check before backend.
        if (
            isinstance(arg.on, list)
            and len(arg.on) == 0
            and arg.left_index == False
            and arg.right_index == False
        ):
            raise IndexError("list index out of range")
        elif (
            isinstance(arg.left_on, list)
            and len(arg.left_on) == 0
            and arg.left_index == False
            and arg.right_index == True
        ):
            raise ValueError(
                'len(left_on) must equal the number of levels in the index of "right"'
            )
        elif (
            isinstance(arg.right_on, list)
            and len(arg.right_on) == 0
            and arg.left_index == True
            and arg.right_index == False
        ):
            raise ValueError(
                'len(right_on) must equal the number of levels in the index of "left"'
            )

        def to_list(x):
            # None can not be used as column name in merge
            if x is None:
                return []
            return x if isinstance(x, list) else [x]

        on = irutils.make_tuple_of_column_names(to_list(arg.on))
        left_on = irutils.make_tuple_of_column_names(to_list(arg.left_on))
        right_on = irutils.make_tuple_of_column_names(to_list(arg.right_on))

        return DataFrame._create(
            ir.join(
                self._value,
                arg.right._value,
                arg.how,
                on,
                left_on,
                arg.left_index,
                right_on,
                arg.right_index,
                left_suffix,
                right_suffix,
            )
        ).__finalize__(op, "merge")

    def notna(self):
        return ~self.isnull()

    def notnull(self):
        return ~self.isnull()

    def pop(self, item):
        out = self[item]
        self.drop(columns=[item], inplace=True)
        return out

    def quantile(self, *args, **kwargs):
        reason = None
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.quantile)

        axis = self._get_axis_number(arg.axis)
        if axis == 1:
            reason = f"unsupported quantile on axis = {arg.axis}"

        # arrow implementation of nearest seems not to
        # return same value as in pandas
        supported_interpolation = {
            "linear",
            "lower",
            "higher",
            "midpoint",
            # "nearest",
        }
        if arg.interpolation not in supported_interpolation:
            reason = f"unsupported 'interpolation' = {arg.interpolation}"

        # dfkl treats default as True
        if arg.numeric_only is pandas_extensions.no_default:
            arg.numeric_only = True
        supported_numeric_only = [None, True]
        if arg.numeric_only not in supported_numeric_only:
            reason = f"unsupported 'numeric_only' = {arg.numeric_only}"

        if arg.method not in {"single", "table"}:
            reason = f"unsupported 'method' = {arg.method}"

        if reason:
            return self._fallback_call_packed(
                "quantile", args, kwargs, reason=reason
            )

        is_scalar = irutils.irable_scalar(arg.q)
        if is_scalar:
            arg.q = float(arg.q)
            CONS = Series._create
        else:
            arg.q = [float(e) for e in arg.q]
            CONS = DataFrame._create
        qs = irutils.make_vector_or_scalar_of_scalar(arg.q)
        return CONS(ir.quantile(self._value, qs, arg.interpolation))

    def query(self, expr, *, inplace=False, local_dict=None, **kwargs):
        reason = None

        if inplace:
            reason = "query with inplace"

        # parameters 'engine' and 'parser' get ignored internally,
        # when some valid values are given.Otherwise, falls back
        # to pandas for error handling etc.
        from pandas.core.computation.check import NUMEXPR_INSTALLED

        known_engines = {"python"}
        if NUMEXPR_INSTALLED:
            known_engines.add("numexpr")
        engine = kwargs.get("engine")
        if engine is None:
            engine = "python"
        if engine not in known_engines:
            reason = f"unknown engine = {engine}"

        known_parsers = {"pandas"}
        parser = kwargs.get("parser")
        if parser is None:
            parser = "pandas"  # default in pandas.eval
        if parser not in known_parsers:
            reason = f"unknown parser = {parser}"

        known_kwargs = {"engine", "parser", "level"}
        tmp = set(kwargs.keys()) - known_kwargs
        if len(tmp) != 0:
            reason = f"unsupported kwargs: {tmp}"

        if not reason:
            level = kwargs.get("level", 0) + 2
            try:
                parser = QueryParser(self, level, local_dict=local_dict)
                key = parser.visit(expr)
                if isinstance(key, Series):
                    dtype = utils._deduce_dtype(key)
                    if dtype is not None and dtype == bool:
                        return DataFrame._create(
                            ir.filter(self._value, key._value)
                        )
                    else:
                        reason = "non-boolean key is given"
                else:
                    reason = (
                        "Non-series parser output of type: "
                        f"{type(key).__name__}"
                    )
            except Exception as e:
                reason = "QueryParser exception: " + str(e)

        kwargs["level"] = kwargs.pop("level", 0) + 4
        return self._fallback_call(
            "query",
            expr,
            inplace=inplace,
            local_dict=local_dict,
            **kwargs,
            __fireducks_reason=reason,
        )

    def rename(
        self,
        mapper=None,
        *,
        index=None,
        columns=None,
        inplace=False,
        axis=None,
        copy=None,
        level=None,
        errors="ignore",
    ):
        mapper, index, columns, axis, copy, level, errors = _unwrap(
            [mapper, index, columns, axis, copy, level, errors]
        )

        reason = None
        _columns = None

        if axis:
            if columns or index:
                raise TypeError(
                    "Cannot specify both 'axis' "
                    "and any of 'index' or 'columns'"
                )

        if mapper:
            if columns or index:
                raise TypeError(
                    "Cannot specify both 'mapper' "
                    "and any of 'index' or 'columns'"
                )
            if axis == 1:
                _columns = mapper

        if columns:
            if index:
                reason = "Unsupported rename with both columns and index"
            _columns = columns

        if isinstance(_columns, dict):
            if errors != "ignore":  # TODO support at kernel side
                reason = f"Unsupported rename with errors='{errors}'"
            if level:
                reason = f"Unsupported rename with level='{level}'"
            if copy is not None and not copy:
                reason = f"Unsupported rename with copy='{copy}'"

            for k in _columns.keys():
                if isinstance(k, tuple):
                    reason = f"MultiIndex key: {k} is not supported"
                    break

            if not reason:
                cols = irutils.make_tuple_of_column_names(
                    list(_columns.keys())
                )
                newcols = irutils.make_tuple_of_column_names(
                    list(_columns.values())
                )
                ret = ir.rename_specified(self._value, cols, newcols)
                return self._create_or_inplace(ret, inplace)
        else:
            reason = (
                "Unsupported rename using columns of "
                + f"type: '{type(_columns).__name__}'"
            )

        fallback = self._get_fallback(inplace)
        return fallback(
            "rename",
            kwargs={
                "mapper": mapper,
                "index": index,
                "columns": columns,
                "inplace": inplace,
                "axis": axis,
                "copy": copy,
                "level": level,
                "errors": errors,
            },
            reason=reason,
        )

    def rolling(self, *args, **kwargs):
        from fireducks.pandas.rolling import DataFrameRolling

        ns = utils.decode_args(args, kwargs, pandas.DataFrame.rolling)
        reason = ns.is_not_default(["win_type"])
        if reason:
            return self._fallback_call_packed(
                "rolling", args, kwargs, reason=reason
            )
        return DataFrameRolling(self, args, kwargs)

    def round(self, decimals=0, *args, **kwargs):
        reason = None
        if args or kwargs:
            reason = "args or kwargs is given"
        if not isinstance(decimals, int):
            reason = (
                "unsupported type for 'decimals' "
                f"parameter: {type(decimals).__name__}"
            )

        if reason:
            return self._fallback_call(
                "round",
                decimals,
                *args,
                **kwargs,
                __fireducks_reason=reason,
            )
        return DataFrame._create(ir.round(self._value, decimals))

    def set_flags(self, *args, **kwargs):
        # Incompatibility: 023
        warnings.warn("set_flags is not supported", DeprecationWarning)
        return self._fallback_call("set_flags", *args, **kwargs)

    @deprecate_nonkeyword_arguments(
        version=None, allowed_args=["self", "keys"]
    )
    def set_index(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.set_index)
        reason = None

        labels = arg.keys
        if isinstance(labels, list):
            if type(labels) is not list:  # FrozenList etc.
                labels = list(labels)
            if len(labels) and is_all_arraylike(labels):
                labels = MultiIndex.from_arrays(labels)

        as_new = isinstance(labels, (Series, Index, MultiIndex, np.ndarray))
        if not as_new and not irutils._is_scalar_or_list_of(
            labels, (str, int)
        ):
            reason = (
                "keys is neither an index-like nor a list of "
                "str, int or index-like"
            )

        if not reason and isinstance(labels, DatetimeIndex):
            # FIXME: frequency information is lost when converting
            # Index -> Series, hence falling back when frequency
            # information is available...
            if labels.freq is not None:
                reason = f"keys is a DatetimeIndex of frequency: {labels.freq}"

        if not reason and isinstance(labels, np.ndarray) and labels.ndim > 1:
            raise ValueError(
                "The parameter 'keys' may be a column key, one-dimensional "
                "array, or a list containing only valid column keys and "
                "one-dimensional arrays."
            )

        if reason:
            return self._fallback_may_inplace(
                "set_index", args, kwargs, pos=3, reason=reason
            )

        drop = bool(arg.drop)
        to_append = bool(arg.append)
        verify_integrity = bool(arg.verify_integrity)
        label_names = []
        if as_new:
            keys = irutils.make_tuple_of_scalars([])
            if isinstance(labels, MultiIndex):
                # keeping original names to be used at backend
                label_names = list(labels.names)
                ncol = len(label_names)
                is_with_dup_names = ncol != len(set(labels.names))
                if is_with_dup_names:
                    # cudf backend doesn't support duplicate names
                    newIndexColumns = labels.to_frame(
                        index=False, name=range(ncol)
                    )
                else:
                    newIndexColumns = labels.to_frame(index=False)
            else:
                newIndexColumns = Series(labels)
        else:
            keys = irutils.make_tuple_of_scalars(labels)
            newIndexColumns = Series([])
        newIndexColumnNames = irutils.make_tuple_of_column_names(label_names)

        # the following boolean parameters are ordered alphabetically as
        # per the .td requirement.  Hence, be careful when changing the
        # order of:  as_new, drop, to_append, verify_integrity
        value = ir.set_index(
            self._value,
            keys,
            newIndexColumns._value,
            newIndexColumnNames,
            as_new,
            drop,
            to_append,
            verify_integrity,
        )
        return self._create_or_inplace(value, arg.inplace)

    @deprecate_nonkeyword_arguments(
        version=None, allowed_args=["self", "level"]
    )
    def reset_index(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.reset_index)
        arg.inplace = validate_bool_kwarg(arg.inplace, "inplace")
        arg.drop = validate_bool_kwarg(arg.drop, "drop")
        if arg.allow_duplicates is pandas_extensions.no_default:
            arg.allow_duplicates = False
        else:
            arg.allow_duplicates = validate_bool_kwarg(
                arg.allow_duplicates, "allow_duplicates"
            )

        # TODO GT #1689
        reason = arg.is_not_default(
            ["level", "col_level", "col_fill", "names"]
        )
        if reason:
            return self._fallback_may_inplace(
                "reset_index", args, kwargs, pos=2, reason=reason
            )

        value = ir.reset_index(
            self._value, arg.allow_duplicates, arg.drop, False
        )
        return self._create_or_inplace(value, arg.inplace)

    @property
    def shape(self) -> tuple[int, int]:
        value = ir.get_shape(self._value)
        shape = fireducks.core.evaluate([value])[0]
        return shape.y, shape.x

    @property
    def size(self) -> int:
        return np.prod(self.shape)

    @property
    def ndim(self) -> int:
        return 2

    @deprecate_nonkeyword_arguments(version=None, allowed_args=["self", "by"])
    def sort_values(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.sort_values)
        if not isinstance(arg.by, list):
            arg.by = [arg.by]
        if not isinstance(arg.ascending, list):
            lst = len(arg.by) if isinstance(arg.by, list) else 1
            arg.ascending = [arg.ascending for _ in range(lst)]

        return self._sort_values(
            args,
            kwargs,
            decoded_args=arg,
            by=arg.by,
            ascending=arg.ascending,
            is_series=False,
        )

    def set_axis(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.set_axis)

        if arg.inplace is True and arg.copy is True:
            raise ValueError("Cannot specify both inplace=True and copy=True")

        reason = None
        if arg.is_not_default(["copy"]) and not arg.copy:
            reason = f"unsupported copy: {arg.copy}"

        if arg.inplace is pandas_extensions.no_default:
            arg.inplace = False

        if not reason:
            labels = arg.labels
            if arg.axis in ("columns", 1):
                if not irutils._is_irable_scalar_arraylike(labels):
                    reason = (
                        f"unsupported value of type: '{type(labels)}'"
                        "for axis=1"
                    )
            elif arg.axis in ("index", 0):
                if isinstance(labels, list):
                    if type(labels) is not list:  # FrozenList etc.
                        labels = list(labels)
                    if len(labels) and is_all_arraylike(labels):
                        labels = MultiIndex.from_arrays(labels)

                if not isinstance(
                    labels, (Series, Index, MultiIndex, range)
                ) and not irutils._is_irable_scalar_arraylike(labels):
                    reason = (
                        "labels is neither an index-like nor a list of "
                        "irable-scalars or index-like"
                    )

                if isinstance(labels, np.ndarray) and labels.ndim > 1:
                    raise ValueError("Index data must be 1-dimensional")
            else:
                raise ValueError(
                    f"No axis named {arg.axis} for object type DataFrame"
                )

        if reason is not None:
            return self._fallback_may_inplace(
                "set_axis", args, kwargs, pos=2, reason=reason
            )

        if arg.axis in ("index", 0):
            # set_index assumes
            #  - range values are existing column names
            #  - input labels are existing column names when they are of
            #    type list/tuple having irable scalars
            labels = (
                Series(labels)
                if isinstance(labels, range)
                or irutils._is_irable_scalar_arraylike(labels)
                else labels
            )
            return self.set_index(labels, inplace=arg.inplace)
        else:
            new_axis = irutils.make_tuple_of_scalars(labels)
            value = ir.rename(self._value, new_axis)
            return self._create_or_inplace(value, arg.inplace)

    def where(self, *args, **kwargs):
        arg = utils.decode_args(args, kwargs, pandas.DataFrame.where)
        arg.inplace = validate_bool_kwarg(arg.inplace, "inplace")

        axis = arg.axis
        cond = arg.cond
        other = arg.other

        reason = arg.is_not_default(["level", "errors", "try_cast"])

        if arg.inplace:
            reason = "inplace is True"
        elif axis is None:
            if isinstance(other, _Scalar):
                reason = "If other is Series, must specify axis=0 or 1"
            else:
                axis = ir.make_scalar_none()
        elif axis == 0:
            axis = irutils.make_scalar(axis)
        else:
            reason = "axis is not 0 or None"

        if isinstance(cond, Series):
            cond = cond._value
            condIsSeries = True
        elif isinstance(cond, DataFrame):
            cond = cond._value
            condIsSeries = False
        else:
            reason = reason or f"type of cond is {type(cond).__name__}"

        if other is pandas_extensions.no_default:
            other = ir.make_scalar_none()
            othertype = "scalar"
        elif irutils.irable_scalar(other):
            other = irutils.make_scalar(other)
            othertype = "scalar"
        elif isinstance(other, _Scalar):
            other = other._value
            othertype = "scalar"
        elif isinstance(other, (Series, DataFrame)):
            other = other._value
            othertype = "table"
        else:
            reason = reason or f"type of other is {type(other).__name__}"

        if reason is not None:
            return self._fallback_may_inplace(
                "where", args, kwargs, pos=2, reason=reason
            )

        if othertype == "scalar":
            value = ir.where_scalar(
                self._value, cond, other, axis, condIsSeries
            )
        else:
            value = ir.where_table(
                self._value, cond, other, axis, condIsSeries
            )

        return self._create_or_inplace(value, arg.inplace)

    #
    # End of python API
    #

    def _build_binop(
        self, rhs, op_str: str, op_original: str, args, kwargs, inplace: bool
    ):
        logger.debug("DataFrame._build_binop: %s", op_str)

        def _fallback(reason, rhs_=rhs):
            fallback = self._get_fallback(inplace)
            return fallback(op_original, (rhs_,) + args, kwargs, reason=reason)

        arg = utils.decode_args(
            (rhs, *args), kwargs, getattr(pandas.DataFrame, op_original)
        )

        # Methods beginning with an underscore do not have 'axis', 'level',
        # and 'fill_value', arguments.
        if not hasattr(arg, "axis"):
            arg.axis = 1
        else:
            # pandas API doc does not menthon about axis=None, but
            # implementation supports it and pandas_tests also uses it.
            arg.axis = (
                self._get_axis_number(arg.axis) if arg.axis is not None else 1
            )

        rhs_t = type(rhs).__name__
        reason = None
        opc = None

        if hasattr(arg, "level") and arg.level is not None:
            reason = "level is not None"
        elif hasattr(arg, "fill_value") and arg.fill_value is not None:
            reason = "fill_value is not None"
        elif isinstance(
            rhs,
            (
                bool,
                int,
                float,
                str,
                np.bool_,
                np.int32,
                np.int64,
                np.float32,
                np.float64,
            ),
        ):
            opc = get_binop_table_scalar(op_str)
            rhs = irutils.make_scalar(rhs)
        elif isinstance(rhs, _Scalar):
            opc = get_binop_table_scalar(op_str)
            rhs = rhs._value
        elif isinstance(rhs, Series):
            if arg.axis == 1:
                reason = "binop among Series with axis=1"
            else:
                opc = get_binop_table_vector(op_str)
                rhs = rhs._value
        elif isinstance(rhs, DataFrame):
            opc = get_binop_table_table(op_str)
            rhs = rhs._value

        if reason is None and opc is None:
            reason = f"unknown op: '{op_str}' on 'DataFrame' and '{rhs_t}'"

        if reason is not None:
            return _fallback(reason)

        op = fireducks.core.build_op(
            opc, [ir.TableType], [self._value, rhs], chaining=True
        )

        if inplace:
            self._rebind(op.outs[0], invalidate_cache=True)
            return self
        return DataFrame._create(op.outs[0])

    def to_csv(self, *args, **kwargs):
        decoded = utils.decode_args(args, kwargs, pandas.DataFrame.to_csv)

        path_or_buf = decoded.path_or_buf

        # NOTE: pandas seems to allow non bool type variable
        index = bool(decoded.index)

        # Workaround: `header` can not be checked by `decoded.is_not_default`
        # because header might be Index or so which can not be compared with
        # default value by `==` operator used in `is_not_default`
        header = decoded.header

        reason = None
        if not (
            isinstance(path_or_buf, (str, os.PathLike)) or path_or_buf is None
        ):
            reason = "path_or_buf is not str or None"
        elif decoded.encoding not in (None, "utf-8", "utf8", "UTF-8", "UTF8"):
            reason = f"encoding is not supported: {decoded.encoding}"
        elif not isinstance(header, bool) or not header:
            reason = "header is not bool or True"
        else:
            reason = decoded.is_not_default(
                exclude=["encoding", "path_or_buf", "index", "header"]
            )

        if reason is not None:
            return self._fallback_call_packed(
                "to_csv", args, kwargs, reason=reason
            )

        if path_or_buf is None:
            result = ir.to_csv(self._value, index)
            return fireducks.core.evaluate([result])[0]

        if isinstance(path_or_buf, os.PathLike):
            path_or_buf = path_or_buf.__fspath__()

        chain = ir.write_csv(self._value, path_or_buf, index)
        fireducks.core.evaluate([chain])

    def to_numpy(self, *args, **kwargs):
        ns = utils.decode_args(args, kwargs, pandas.DataFrame.to_numpy)
        reason = ns.is_not_default(
            [
                "dtype",
                "na_value",
                # Because ns.copy=False does not ensure no copy in pandas and
                # fireducks always copies, ns.copy can be ignored.
            ]
        )

        if not reason:
            if fireducks.core.get_ir_prop().has_metadata:
                target_types = [
                    np.int8,
                    np.int16,
                    np.int32,
                    np.int64,
                    np.uint8,
                    np.uint16,
                    np.uint32,
                    np.uint64,
                    np.float32,
                    np.float64,
                ]
                col_dtypes = list(self.dtypes)
                is_numeric = len(col_dtypes) > 0 and np.all(
                    [i in target_types for i in col_dtypes]
                )
                # fallback in case any non-numeric column exists
                if not is_numeric:
                    reason = "to_numpy with non-numeric column"

        if reason is not None:
            return self._fallback_call_packed(
                "to_numpy", args, kwargs, reason=reason
            )
        value = ir.to_numpy(self._value)
        # Workaround: For single column dataframe, dfkl's `ir.to_numpy`
        # returns 1-dim array as Series.to_numpy.
        np_arr = fireducks.core.evaluate([value])[0]
        return np_arr.reshape(len(np_arr), 1) if np_arr.ndim == 1 else np_arr

    def __array__(self, *args, **kwargs):
        ns = utils.decode_args(args, kwargs, pandas.DataFrame.__array__)

        reason = ns.is_not_default(["dtype"])
        if reason is not None:
            return self._fallback_call_packed(
                "__array__", args, kwargs, reason=reason
            )
        return self.to_numpy()

    @property
    def values(self):
        """Return a Numpy representation of the DataFrame."""
        logger.debug("DataFrame.values")
        if self._fireducks_meta.is_cached():
            return utils._wrap(self._fireducks_meta.get_cache().values)

        reason = None

        if fireducks.core.get_ir_prop().has_metadata:
            target_types = [
                np.int8,
                np.int16,
                np.int32,
                np.int64,
                np.uint8,
                np.uint16,
                np.uint32,
                np.uint64,
                np.float32,
                np.float64,
            ]
            col_dtypes = list(self.dtypes)
            is_numeric = len(col_dtypes) > 0 and np.all(
                [i in target_types for i in col_dtypes]
            )
            # for non-numeric cases, pandas output might differ
            # for to_numpy() and values
            if not is_numeric:
                reason = "DataFrame.values with non-numeric column"

        if reason is not None:
            return utils.fallback_attr(
                self._unwrap,
                "values",
                reason=reason,
            )
        value = ir.to_numpy(self._value)
        # Workaround: For single column dataframe, dfkl's `ir.to_numpy`
        # returns 1-dim array as Series.to_numpy.
        np_arr = fireducks.core.evaluate([value])[0]
        return np_arr.reshape(len(np_arr), 1) if np_arr.ndim == 1 else np_arr


def _to_pandas_frame_metadata(value, options=None):
    v0, v1 = ir.to_pandas_frame_metadata(value)
    df, meta = fireducks.core.evaluate([v0, v1], options=options)
    logger.debug("to_pandas_frame_metadata: meta=%s", meta)
    with tracing.scope(tracing.Level.VERBOSE, "to_pandas:metadata.apply"):
        return IRMetadataWrapper(meta).apply(df)
