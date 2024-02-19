# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

import functools
import inspect
import logging
import types
import weakref

import numpy as np
import pandas.core.resample
import pandas
from collections.abc import Iterable

import fireducks.core
import fireducks.pandas
import fireducks.fallback as ff

from fireducks.fallback import (
    FallbackManager,
    prohibit_fallback,
)

__all__ = ["FallbackManager", "prohibit_fallback", "_pd_version_under2"]

try:
    import xarray

    HAS_XARRAY = True
except ModuleNotFoundError:
    HAS_XARRAY = False

import firefw as fire

from fireducks.pandas.binop import (
    COMPARISON_BINOPS,
    LOGICAL_BINOPS,
    REV_LOGICAL_BINOPS,
    INPLACE_LOGICAL_BINOPS,
)

from fireducks.irutils import (
    _is_str_list,
    make_tuple_of_column_names,
    make_tuple_of_vector_or_scalar_of_str,
)

logger = logging.getLogger(__name__)


def is_pandas_version_under_v2():
    from pandas.util.version import Version

    pdlv = Version(Version(pandas.__version__).base_version)
    return pdlv < Version("2")


_pd_version_under2 = is_pandas_version_under_v2()


def _is_str_list_or_index(obj):
    if isinstance(obj, fireducks.pandas.wrappers.Index):
        obj = list(obj)
    return _is_str_list(obj)


def fallback_attr(
    fallbacker, name, reason=None, *, stacklevel=0, wrap_func=None
):
    wrap_func = wrap_func or _wrap
    options = fireducks.core.get_fireducks_options()
    return ff.fallback_attr(
        fallbacker,
        name,
        reason,
        stacklevel=stacklevel,
        wrap_func=wrap_func,
        unwrap_func=_unwrap,
        log_lineno=options.fallback_lineno,
        warn_fallback=options.warn_fallback,
    )


# Deprecated. Use fallback_call_packed.
def fallback_call(
    __fireducks_fallbacker,
    __fireducks_method,
    *args,
    __fireducks_reason=None,
    **kwargs,
):
    """
    Fallback a method call

    After resolving attribute, call it with arguments.

    Parameters
    ----------
    See above.  To avoid name conflict, prefix `__fireducks` is uses.
    """
    return fallback_call_packed(
        __fireducks_fallbacker,
        __fireducks_method,
        args,
        kwargs,
        reason=__fireducks_reason,
    )


def fallback_call_packed(
    fallbacker, method, args=None, kwargs=None, *, reason=None, stacklevel=7
):
    options = fireducks.core.get_fireducks_options()
    return ff.fallback_call(
        fallbacker,
        method,
        args,
        kwargs,
        reason=reason,
        stacklevel=stacklevel,
        wrap_func=_wrap,
        unwrap_func=_unwrap,
        log_lineno=options.fallback_lineno,
        warn_fallback=options.warn_fallback,
    )


# TODO: Experimental
# Current implmentaion returns bool when value is defined by logical binop on
# vector.
def _infer_dtype(value: fire.Value):
    opcode = value.get_def().opcode
    logger.debug("_infer_dtype: opcode=%s", opcode.name)
    logicals = [
        f"fireducks.{op}.vector"
        for op in COMPARISON_BINOPS
        + LOGICAL_BINOPS
        + REV_LOGICAL_BINOPS
        + INPLACE_LOGICAL_BINOPS
    ] + [
        "fireducks.isin",
        "fireducks.isnull",
        "fireducks.str_contains",
        "fireducks.str_endswith",
        "fireducks.str_startswith",
        "fireducks.str_unary_bool_returning_method",
    ]
    for op in logicals:
        if op in opcode.name:
            return np.dtype(bool)

    # TODO: and,or,xor also should infer with inputs
    if opcode.name == "fireducks.invert":
        return _infer_dtype(value.get_def().ins[0])

    return None  # unknown


def _deduce_dtype(key):
    dtype = None  # when type deduction is not possible

    # deduce from cached data (if available)
    if key._fireducks_meta.is_cached():
        dtype = key._fireducks_meta.get_cache().dtypes

    # infer from OPCODE, when cache data is not available
    if dtype is None:
        dtype = _infer_dtype(key._value)
        logger.debug("inferred dtype: %s", dtype)

    # if still not known, evaluate the OP and deduce from result metadata
    if dtype is None and fireducks.core.get_ir_prop().has_metadata:
        dtypes, unsupported = key._get_metadata().dtypes
        if len(unsupported) == 0:
            dtype = dtypes[0]

    return dtype


#
# Type utils
#


def _is_list_like_of(obj, types):
    return pandas.api.types.is_list_like(obj) and all(
        [isinstance(x, types) for x in obj]
    )


def _is_fireducks_class(cls):
    return cls is fireducks.pandas.DataFrame or cls is fireducks.pandas.Series


def _hasattr(obj, name):
    """Check if obj has name without calling obj.__getattr__

    Builtin function `hasattr` calls obj.__getattr__ when obj does not have
    name. In fireducks it may fallback to pandas. This method can be used when
    you just want to know if obj has name.
    """
    try:
        object.__getattribute__(obj, name)
        return True
    except AttributeError:
        pass
    return False


def _fireducks_class(pandas_class):
    if pandas_class is pandas.Series:
        return fireducks.pandas.Series
    elif pandas_class is pandas.DataFrame:
        return fireducks.pandas.DataFrame
    elif pandas_class is pandas.CategoricalIndex:
        return fireducks.pandas.CategoricalIndex
    elif pandas_class is pandas.DatetimeIndex:
        return fireducks.pandas.DatetimeIndex
    elif pandas_class is pandas.IntervalIndex:
        return fireducks.pandas.IntervalIndex
    elif pandas_class is pandas.MultiIndex:
        return fireducks.pandas.MultiIndex
    elif (
        _pd_version_under2
        and pandas_class is pandas.core.indexes.numeric.NumericIndex
    ):
        return fireducks.pandas.NumericIndex
    elif _pd_version_under2 and pandas_class is pandas.core.api.Int64Index:
        return fireducks.pandas.Int64Index
    elif _pd_version_under2 and pandas_class is pandas.core.api.UInt64Index:
        return fireducks.pandas.UInt64Index
    elif _pd_version_under2 and pandas_class is pandas.core.api.Float64Index:
        return fireducks.pandas.Float64Index
    elif pandas_class is pandas.PeriodIndex:
        return fireducks.pandas.PeriodIndex
    elif pandas_class is pandas.RangeIndex:
        return fireducks.pandas.RangeIndex
    elif pandas_class is pandas.TimedeltaIndex:
        return fireducks.pandas.TimedeltaIndex
    elif pandas_class is pandas.Index:
        return fireducks.pandas.Index
    elif pandas_class is pandas.Categorical:
        return fireducks.pandas.Categorical
    elif pandas_class is pandas.core.groupby.indexing.GroupByNthSelector:
        return PandasCallableWrapper
    elif issubclass(
        pandas_class,
        (
            pandas.core.arrays.categorical.CategoricalAccessor,
            pandas.core.groupby.generic.DataFrameGroupBy,
            pandas.core.groupby.grouper.Grouping,
            pandas.core.groupby.ops.BaseGrouper,
            pandas.core.indexes.accessors.DatetimeProperties,
            pandas.core.resample.Resampler,
            pandas.io.formats.printing.PrettyDict,
        ),
    ):
        return PandasWrapper
    elif HAS_XARRAY and issubclass(
        pandas_class,
        (
            xarray.core.dataarray.DataArray,
            xarray.core.dataset.Dataset,
        ),
    ):
        return PandasWrapper
    elif issubclass(pandas_class, types.GeneratorType):
        return PandasGeneratorWrapper
    return pandas_class


def _pandas_class(fireducks_class):
    if fireducks_class is fireducks.pandas.DataFrame:
        return pandas.DataFrame
    elif fireducks_class is fireducks.pandas.Series:
        return pandas.Series
    raise RuntimeError(f"Unknown fireducks class: {fireducks_class}")


#
# Utils
#


def is_eq(left, right):
    if left is None and right is None:
        return True
    eq = left == right
    return all(eq) if isinstance(eq, Iterable) else eq


class DecodedArgs:
    def __init__(self, defaults, arguments):
        self._defaults = defaults
        for k, v in arguments.items():
            if k != "self":
                setattr(self, k, v)

    def is_not_default(self, check_list=[], exclude=[]):
        if not check_list:
            exclude += ["self"]
            check_list = set(self._defaults.keys()) - set(exclude)

        for arg in check_list:
            if arg in self._defaults:
                default = self._defaults[arg]
                arg_val = getattr(self, arg)
                if is_eq(default, arg_val):
                    continue
                return f"{arg} is not {default}"
            else:
                return f"{arg} is not in kwargs"
        return None


# decode_args() cache
_decode_args_cache = {}


def decode_args(fargs, fkwargs, pandas_func):
    """Decode real arguments to formal arguments via signature

    This function decodes args according to the signature of pandas_func.

    Parameters
    ----------
    fargs: args to decode
    fkwargs: kwargs to decode
    pandas_func: pandas function to get signature
    """

    global _decode_args_cache
    pandas_sig = _decode_args_cache.get(pandas_func, None)
    if pandas_sig is None:
        # Follow __wrappped__ attribute created by functools.wraps
        wrapped = inspect.unwrap(pandas_func)
        pandas_sig = inspect.signature(wrapped)
        _decode_args_cache[pandas_func] = pandas_sig

    if "self" in pandas_sig.parameters:
        # bind self to None
        bound = pandas_sig.bind(None, *fargs, **fkwargs)
    else:
        bound = pandas_sig.bind(*fargs, **fkwargs)

    bound.apply_defaults()
    defaults = {}
    for k, v in pandas_sig.parameters.items():
        if k == "kwargs" and v.default is inspect._empty:
            defaults[k] = {}
        else:
            defaults[k] = v.default

    return DecodedArgs(defaults, bound.arguments)


#
# Utils for fallback
#


def _setup_PandasWrapper(cls):
    def wrap_method(method_name: str):
        @functools.wraps(method_name)
        def wrapped_method(self, *args, **kwargs):
            attr = getattr(self._pandas_obj, method_name)
            ret = attr(*_unwrap(args), **_unwrap(kwargs))
            return _wrap(ret)

        return wrapped_method

    methods = [
        # operator
        "__add__",
        "__and__",
        "__div__",
        "__divmod__",
        "__eq__",
        "__floordiv__",
        "__ge__",
        "__gt__",
        "__iadd__",
        "__iand__",
        "__idiv__",
        "__idivmod__",
        "__ifloordiv__",
        "__ilshift__",
        "__imod__",
        "__imul__",
        "__invert__",
        "__ior__",
        "__ipow__",
        "__irshift__",
        "__isub__",
        "__itruediv__",
        "__ixor__",
        "__le__",
        "__lshift__",
        "__lt__",
        "__mod__",
        "__mul__",
        "__ne__",
        "__neg__",
        "__or__",
        "__pow__",
        "__radd__",
        "__rand__",
        "__rdiv__",
        "__rdivmod__",
        "__rfloorfiv__",
        "__rlshift__",
        "__rmod__",
        "__rmul__",
        "__ror__",
        "__rpow__",
        "__rrshift__",
        "__rshift__",
        "__rsub__",
        "__rtruediv__",
        "__rxor__",
        "__sub__",
        "__truediv__",
        "__xor__",
        # others
        "__dir__",
        "__iter__",
        "__repr__",
    ]  # yapf: disable

    for method_name in methods:
        wrapped = wrap_method(method_name)
        type.__setattr__(cls, method_name, wrapped)
    return cls


@_setup_PandasWrapper
class PandasWrapper:
    """PandasWrapper wraps a pandas object.

    All attribute access are redirect to the wrapped pandas object, and
    returned value is wrapped to a fireducks object.
    """

    def __init__(self, _pandas_obj=None, class_=None):
        assert _pandas_obj is not None
        object.__setattr__(self, "_pandas_obj", _pandas_obj)

        class_ = class_ or type(_pandas_obj)
        object.__setattr__(self, "_wrapped_class", class_)

        # Add wrapper object reference to pandas object
        try:
            object.__setattr__(
                _pandas_obj, "_fireducks_wrapper", weakref.ref(self)
            )
        except AttributeError:
            # Returns AttributeError if _pandas_obj has __slots__.
            pass

    @property
    def __class__(self):
        return self._wrapped_class

    def __bool__(self):
        return bool(self._pandas_obj)

    def __getattr__(self, name):
        reason = (
            f"{type(self._pandas_obj).__name__}.__getattr__ for {name}"
            " is called"
        )
        return fallback_attr(self._unwrap, name, reason=reason)

    def __setattr__(self, name, value):
        setattr(self._pandas_obj, name, value)

    def __getitem__(self, key):
        return _wrap(self._pandas_obj[key])

    def __setitem__(self, key, value):
        self._pandas_obj[key] = _unwrap(value)

    def __len__(self):
        return len(self._pandas_obj)

    def _unwrap(self, reason=None):
        return self._pandas_obj


class PandasCallableWrapper(PandasWrapper):
    def __call__(self, *args, **kwargs):
        return _wrap(self._pandas_obj(*args, **kwargs))


class PandasClassWrapperMetaclass(type):
    def __getattr__(cls, name):
        def _unwrap(reason=None):
            return cls._pandas_cls

        reason = f"{cls._pandas_cls.__name__}.__getattr__ for {name} is called"
        return fallback_attr(_unwrap, name, reason=reason)


class PandasClassWrapper(PandasWrapper, metaclass=PandasClassWrapperMetaclass):
    def __init__(self, *args, _pandas_obj=None, **kwargs):
        if _pandas_obj is None:
            _pandas_obj = self._pandas_cls(*_unwrap(args), **_unwrap(kwargs))
        super().__init__(_pandas_obj=_pandas_obj)

    @property
    def __class__(self):
        return self._pandas_cls


class PandasGeneratorWrapper:
    def __init__(self, _pandas_obj=None):
        assert _pandas_obj is not None
        object.__setattr__(self, "_pandas_obj", _pandas_obj)

    def __iter__(self):
        self._pandas_obj = iter(self._pandas_obj)
        return self

    def __next__(self):
        return _wrap(next(self._pandas_obj))

    def _unwrap(self, reason=None):
        raise NotImplementedError()


def install_wrapper(cls, name, wrapper, parent_class=None, override=False):
    """
    Set `cls`'s attribute `name` to `wrapper` as it looks like `name` of
    `parent_class`
    """

    if not override and _hasattr(cls, name):
        logger.debug(
            "install_wrapper: skip %s.%s to prevent override",
            cls.__name__,
            name,
        )
        return

    if parent_class is not None:
        # At the moment, we support only wrapper of FunctionType
        assert isinstance(wrapper, types.FunctionType)

        wrapped = getattr(parent_class, name)
        logger.debug(
            "install_wrapper: %s.%s.%s (wrapped: %s)",
            cls.__module__,
            cls.__name__,
            name,
            wrapped,
        )
        if isinstance(wrapped, types.FunctionType):
            functools.update_wrapper(wrapper, wrapped)
        elif isinstance(wrapped, property):
            # Expect that wrapped.fget returns callable
            wrapper.__name__ = name
            wrapper.__qualname__ = f"{parent_class.__name__}.{name}"

    type.__setattr__(cls, name, wrapper)


def install_fallback(cls, name, parent=None, override=False):
    """
    Install fallback to `cls` on name.
    """

    def wrapper(self, *args, **kwargs):
        reason = (
            "Installed fallback wrapper"
            f" for {cls.__name__}.{name} is called"
        )
        assert hasattr(self, "_unwrap")
        return fallback_call_packed(
            self._unwrap,
            name,
            _unwrap(args),
            _unwrap(kwargs),
            reason=reason,
            stacklevel=6,
        )

    install_wrapper(cls, name, wrapper, parent, override)


def install_fallbacks(cls, names, parent=None, override=False):
    for name in names:
        install_fallback(cls, name, parent, override)


def _unwrap(obj, *, reason=None, recursive=True):
    import collections

    if isinstance(obj, type):
        return obj

    if hasattr(obj, "_unwrap"):
        return obj._unwrap(reason=reason)

    if not recursive:
        return obj

    if isinstance(obj, list):
        return [_unwrap(x, reason=reason) for x in obj]

    # Do not unwrap NamedAgg to prevent it from converting to tuple. GT #843
    from pandas.core.groupby.generic import NamedAgg

    if isinstance(obj, NamedAgg):
        return obj

    if isinstance(obj, tuple):
        from pandas.core.dtypes.inference import is_named_tuple

        if is_named_tuple(obj) and hasattr(obj, "_make"):
            # namedtuple
            return obj._make([_unwrap(x, reason=reason) for x in obj])
        else:
            # tuple
            return tuple(_unwrap(x, reason=reason) for x in obj)

    if isinstance(obj, collections.abc.Mapping):
        dic = {_unwrap(k): _unwrap(v, reason=reason) for k, v in obj.items()}
        if hasattr(obj, "default_factory"):
            return collections.defaultdict(obj.default_factory, dic)
        return dic

    return obj


class ReadOnlyAccessor:
    """ReadOnlyAccessor wraps an accessor of pandas.

    In pandas, an accessor is created from DataFrame or Series. An accessor may
    have methods or attributes to return a subset of the DataFrame/Series from
    which it is created. It may also have methods to update the
    DataFrame/Series. Examples are _LocIndexer create by DataFrame.loc,
    StringMethods created from Series.str.

    ReadOnlyAccessor wraps such pandas's accessor to wrap pandas's
    DataFrame/Series returned from it to fireducks's one. ReadOnlyAccessor
    supports pandas's accessor which has only read access. That means it does
    not support update of the dataframe/series through an accessor.

    Be careful to add methods such as `__setattr__` and `__setitem__`. It may
    update the original object In that case, simple fallback does not work. See
    `DataFrame._fallback_mutating_method`.
    """

    def _unwrap(self, reason):
        raise NotImplementedError()

    def __getattr__(self, name):
        reason = "ReadOnlyAccessor.__getattr__ is called"
        return fallback_attr(self._unwrap, name, reason)

    def __getitem__(self, key):
        reason = "ReadOnlyAccessor.__getitem__ is called"
        return fallback_call(
            self._unwrap, "__getitem__", key, __fireducks_reason=reason
        )


def _wrap(obj):
    from fireducks.pandas.api import from_pandas

    obj_type = type(obj)
    logger.debug("_wrap: %s", obj_type)
    if isinstance(obj, pandas.DataFrame) or isinstance(obj, pandas.Series):
        return from_pandas(obj)

    assert not isinstance(obj, PandasWrapper)

    if hasattr(obj, "_fireducks_wrapper"):
        # Return wrapper if this pandas object has a valid wrapper reference.
        # Make sure the reference is not NONE, because the reference is a
        # weakref.
        wrapper_obj = obj._fireducks_wrapper()
        if wrapper_obj is not None:
            return wrapper_obj

    wrapper_class = _fireducks_class(obj_type)
    if wrapper_class is not obj_type:
        return wrapper_class(_pandas_obj=obj)

    if isinstance(obj, list):
        # Call the constructor so that classes that inherit from list can also
        # be supported.  - e.g. DataFrame.index.names returns
        # pandas.core.indexes.frozen.FrozenList which inherits from list.
        return obj_type(_wrap(x) for x in obj)
    if isinstance(obj, tuple):
        return tuple(_wrap(x) for x in obj)

    if isinstance(obj, dict):
        return {k: _wrap(v) for k, v in obj.items()}

    if isinstance(obj, type):
        return obj

    return obj


def _get_pandas_module(reason=None):
    return pandas


def apply_dict_on_series(dict_map, ser):
    left = ser.reset_index()
    left["order"] = range(len(left))
    left.columns = ["index", "key", "order"]

    right = fireducks.pandas.DataFrame()
    right["key"] = list(dict_map.keys())
    right["val"] = list(dict_map.values())

    return (
        left.merge(right, on="key", how="left")
        .sort_values("order")
        .set_index("index")["val"]
    )


class AggArgs:
    def __init__(self, funcs, columns, relabels):
        self.funcs = funcs
        self.columns = columns
        self.relabels = relabels

    def to_ir(self):
        funcs = make_tuple_of_vector_or_scalar_of_str(self.funcs)
        columns = make_tuple_of_column_names(self.columns)
        relabels = make_tuple_of_column_names(self.relabels)
        return funcs, columns, relabels

    def debug_print(self):
        for t in ["funcs", "columns", "relabels"]:
            print(f"{t} -> {getattr(self, t)}")  # noqa

    @classmethod
    def from_dict(cls, dic: dict):
        args = AggArgs([], [], [])
        for col, methods in dic.items():
            args.columns += [col]
            args.funcs += [methods]
        return args

    @classmethod
    def from_named(cls, kwargs):
        msg = "Must provide 'func' or tuples of '(column, aggfunc)"
        if not kwargs:
            raise TypeError(msg)

        args = AggArgs([], [], [])
        for relabel, tmp in kwargs.items():
            if not isinstance(tmp, tuple) or len(tmp) != 2:
                raise TypeError(msg)
            column, func = tmp
            args.funcs += [func]
            args.columns += [column]
            args.relabels += [relabel]
        return args


def make_agg_args(func, *args, **kwargs):
    if func is None:
        assert not args
        return AggArgs.from_named(kwargs)

    # When func is not None, args and kwargs are arguments of func.
    # Not supported.
    if args or kwargs:
        return None

    if isinstance(func, dict):
        return AggArgs.from_dict(func)

    if isinstance(func, str) or _is_str_list(func):
        return AggArgs([func], [], [])

    return None


def is_supported_df_agg_funcs(funcs):
    supported_backends_funcs = {
        "sum",
        "max",
        "min",
        "size",
        "count",
        "nunique",
        "mean",
        "median",
        "std",
        "var",
        "all",
        "any",
        "skew",
        "kurt",
        "quantile",
    }  # yapf: disable

    def is_supported(f):
        return isinstance(f, str) and f in supported_backends_funcs

    flat = sum([f if isinstance(f, list) else [f] for f in funcs], [])
    return all([is_supported(f) for f in flat])


def is_int_or_none_slice(s: slice) -> bool:
    return all(
        [(isinstance(x, int) or x is None) for x in [s.start, s.stop, s.step]]
    )
