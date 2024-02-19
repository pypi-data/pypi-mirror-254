# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

from collections import abc
import os
import logging

from pandas.io.common import is_url, is_fsspec_url
from pandas.core.dtypes.common import is_scalar
import pandas._libs.missing as libmissing

from firefw import tracing

with tracing.scope(tracing.Level.DEFAULT, "import pandas"):
    import pandas
    from pandas.util._decorators import deprecate_nonkeyword_arguments
    import pandas.api.extensions as pandas_extensions

from fireducks import ir, irutils
import fireducks.core
from fireducks.pandas.frame import DataFrame
from fireducks.pandas.series import Series
import fireducks.pandas.utils as utils

logger = logging.getLogger(__name__)

#
# FireDucks API
#


def from_pandas(obj):
    logger.debug("from_pandas: %s", type(obj))

    if isinstance(obj, pandas.DataFrame):
        return DataFrame.from_pandas(obj)
    elif isinstance(obj, pandas.Series):
        return Series.from_pandas(obj)
    raise RuntimeError(
        "fireducks.from_panad: unknown object is given: " f"{type(obj)}"
    )


#
# Pandas copmat API
#


@deprecate_nonkeyword_arguments(version=None, allowed_args=["objs"])
def concat(*args, **kwargs):
    arg = utils.decode_args(args, kwargs, pandas.concat)
    if isinstance(arg.objs, abc.Mapping):
        if arg.keys is None:
            arg.keys = list(arg.objs.keys())
        arg.objs = [arg.objs[k] for k in arg.keys]
    else:
        # If `objs` is a generator expression, we can get the values from
        # `objs` just once, so overwrite it with the expanded list.
        arg.objs = list(arg.objs)
        args = (arg.objs,) + args[1:]

    if not arg.objs:
        raise ValueError("No objects to concatenate")

    class Concat:
        def __init__(self, objs):
            self.objs = objs

    op = Concat(arg.objs)
    cls = None
    if all([isinstance(obj, DataFrame) for obj in arg.objs]):
        cls = DataFrame
    if all([isinstance(obj, Series) for obj in arg.objs]):
        cls = Series

    if cls is None:
        reason = "objs are not DataFrame or Series"
    else:
        reason = arg.is_not_default(
            [
                "axis",
                "join",
                # "ignore_index",
                "keys",
                "levels",
                "names",
                "verify_integrity",
                "sort",
                "copy",
            ]
        )

    if reason:
        return utils.fallback_call_packed(
            utils._get_pandas_module,
            "concat",
            args,
            kwargs,
            reason=reason,
        ).__finalize__(op, method="concat")

    objs = irutils.make_tuple_of_tables(arg.objs)
    return cls._create(
        ir.concat(
            objs, ignore_index=arg.ignore_index, no_align=(cls == Series)
        )
    ).__finalize__(op, method="concat")


def get_dummies(data, *args, **kwargs):
    reason = None

    if args:
        reason = "args are specified"

    drop_first = False
    if kwargs:
        if len(kwargs) == 1 and "drop_first" in kwargs:
            drop_first = kwargs.get("drop_first")
        else:
            reason = (
                f"unsupported kwargs '{list(kwargs.keys())}' are specified"
            )

    # if isinstance(data, (DataFrame, Series)):
    if not isinstance(data, DataFrame):
        reason = "input is not a DataFrame"

    if reason is None:
        value = ir.get_dummies(data._value, drop_first)
        return DataFrame._create(value)

    return utils.fallback_call(
        utils._get_pandas_module,
        "get_dummies",
        data,
        *args,
        **kwargs,
        __fireducks_reason=reason,
    )


def isnull(obj):
    if is_scalar(obj):
        return libmissing.checknull(obj)
    elif isinstance(obj, type):
        return False
    elif isinstance(obj, (DataFrame, Series)):
        return obj.isnull()

    return utils.fallback_call(
        utils._get_pandas_module,
        "isnull",
        obj,
        __fireducks_reason="obj is not DataFrame or Series",
    )


isna = isnull


def melt(frame, *args, **kwargs):
    if isinstance(frame, DataFrame):
        return frame.melt(*args, **kwargs)

    return utils.fallback_call(
        utils._get_pandas_module,
        "melt",
        frame,
        *args,
        __fireducks_reason="obj is not DataFrame",
        **kwargs,
    )


def merge(left, right, **kwargs):
    return left.merge(right, **kwargs)


def notna(obj):
    if isinstance(obj, (DataFrame, Series)):
        return ~(obj.isnull())

    return utils.fallback_call(
        utils._get_pandas_module,
        "notna",
        obj,
        __fireducks_reason="obj is not DataFrame or Series",
    )


notnull = notna


def read_csv(*args, **kwargs):
    decoded = utils.decode_args(args, kwargs, pandas.read_csv)

    names = decoded.names
    filepath_or_buffer = decoded.filepath_or_buffer
    index_col = decoded.index_col
    usecols = decoded.usecols
    dtype = decoded.dtype
    sep = decoded.sep
    delimiter = decoded.delimiter

    reason = None
    if names is not pandas_extensions.no_default and not irutils._is_str_list(
        names
    ):
        reason = "names is not a list of string"
    elif not isinstance(filepath_or_buffer, str):
        reason = "filepath_or_buffer is not filepath"
    elif index_col is not None and not isinstance(index_col, int):
        reason = "index_col is not int or None"
    elif usecols is not None and not irutils._is_str_list(usecols):
        reason = "usecols is not a list of string"
    elif (
        dtype is not None
        and not isinstance(dtype, dict)
        and not irutils.is_supported_dtype(dtype)
    ):
        reason = f"dtype is not supported: {dtype}"
    elif isinstance(dtype, dict):
        for key, typ in dtype.items():
            if not isinstance(key, str):
                reason = f"column name of dtype is not string: {key}"
            elif not irutils.is_supported_dtype(typ):
                reason = f"dtype is not supported: {typ}"
        if hasattr(dtype, "default_factory"):  # defaultdict
            default_dtype = dtype.default_factory()
            if not irutils.is_supported_dtype(default_dtype):
                reason = f"default dtype is not supported: {default_dtype}"

    if reason is None:
        reason = decoded.is_not_default(
            exclude=[
                "names",
                "filepath_or_buffer",
                "index_col",
                "usecols",
                "dtype",
                "sep",
                "delimiter",
            ]
        )

    if reason is None:
        path = os.path.expanduser(filepath_or_buffer)
        if is_url(path):
            reason = "path is url"
        if is_fsspec_url(path):
            reason = "seems like fsspec path"

    if reason is not None:
        return utils.fallback_call_packed(
            utils._get_pandas_module,
            "read_csv",
            args,
            kwargs,
            reason=reason,
        )

    # when include_columns is empty, all columns are returned
    include_columns = [] if usecols is None else usecols

    from fireducks.fireducks_ext import ReadCSVOptions

    options = ReadCSVOptions()
    if names is not pandas_extensions.no_default:
        options.names = names
    if index_col is not None:
        options.index_col = index_col
    if include_columns:
        options.include_columns = include_columns
    if delimiter is None:
        delimiter = sep
    if delimiter is pandas_extensions.no_default:
        delimiter = ","
    options.delimiter = delimiter

    if isinstance(dtype, dict):
        for k, v in dtype.items():
            options.set_column_type(k, irutils.to_supported_dtype(v))
        if hasattr(dtype, "default_factory"):  # defaultdict
            options.default_dtype = irutils.to_supported_dtype(
                dtype.default_factory()
            )
    elif dtype is not None:
        options.default_dtype = irutils.to_supported_dtype(dtype)

    options = fireducks.core.make_available_value(
        options, ir.ReadCSVOptionsType
    )

    value = ir.read_csv(filepath_or_buffer, options)
    return DataFrame._create(value)


def read_parquet(path, engine="auto", *args, **kwargs):
    reason = None

    # engine=pyarrow should be supported?
    if engine != "auto" and engine != "pyarrow":
        reason = f"engine is not auto: {engine}"

    if not isinstance(path, str) or args or kwargs:
        reason = "args or kwargs is used"

    if isinstance(path, str):
        path = os.path.expanduser(path)
        if os.path.isdir(path):
            reason = "path is directory"
        if is_url(path):
            reason = "path is url"
        if is_fsspec_url(path):
            reason = "seems like fsspec path"

    if reason is not None:
        return utils.fallback_call(
            utils._get_pandas_module,
            "read_parquet",
            path,
            engine,
            *args,
            **kwargs,
            __fireducks_reason=reason,
        )

    return DataFrame._create(ir.read_parquet(path))


# pandas.io.to_parquet is not found in the API document as far as we know. But
# pandas_tests uses it. We provide it as fireducks.pandas.to_parquet because
# fireducks does not provide fireducks.pandas.io package at the moment.
def to_parquet(*args, **kwargs):
    def get_module(reason=None):
        from pandas.io import parquet

        return parquet

    return utils.fallback_call(
        get_module,
        "to_parquet",
        *args,
        **kwargs,
        __fireducks_reason="to_parquet is fallback",
    )


def to_pickle(obj, *args, **kwargs):
    logger.debug("to_pickle")
    pandas.to_pickle(utils._unwrap(obj), *args, **kwargs)
