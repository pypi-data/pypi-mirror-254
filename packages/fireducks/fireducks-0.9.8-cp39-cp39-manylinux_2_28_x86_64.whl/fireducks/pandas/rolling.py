# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

from abc import abstractmethod
import pandas
from fireducks import ir, irutils
from fireducks.pandas import utils, DataFrame, Series

# https://pandas.pydata.org/docs/reference/window.html
_known_funcs = {
    "count": "count",
    "sum": "sum",
    "mean": "mean",
    "median": "median",
    "var": "variance",
    "std": "stddev",
    "min": "min",
    "max": "max",
    "corr": None,
    "skew": None,
    "kurt": None,
    "quantile": None,
    "sem": None,
    "rank": None,
}


def to_supported_function(func):
    return _known_funcs.get(func)


class Rolling:
    def __init__(self, obj, args, kwargs):
        self._obj = obj
        self._rolling_args = args
        self._rolling_kwargs = kwargs

    def _unwrap(self, reason=None):
        return self._obj._fallback_call_packed(
            "rolling", self._rolling_args, self._rolling_kwargs, reason=reason
        )

    def _fallback_call(self, method, args, kwargs, *, reason=None):
        return utils.fallback_call_packed(
            self._unwrap, method, args, kwargs, reason=reason
        )

    @abstractmethod
    def aggregate(self, *args, **kwargs):
        raise NotImplementedError()

    agg = aggregate

    def count(self):
        return self.aggregate("count")

    def sum(self):
        return self.aggregate("sum")

    def mean(self):
        return self.aggregate("mean")

    def median(self):
        return self.aggregate("median")

    def min(self):
        return self.aggregate("min")

    def max(self):
        return self.aggregate("max")


class DataFrameRolling(Rolling):
    def aggregate(self, *args, **kwargs):
        ns = utils.decode_args(
            args, kwargs, pandas.core.window.rolling.Rolling.aggregate
        )

        rolling_ns = utils.decode_args(
            self._rolling_args, self._rolling_kwargs, pandas.DataFrame.rolling
        )

        if not isinstance(rolling_ns.window, int):
            reason = "window is not int"
        else:
            reason = rolling_ns.is_not_default(
                [
                    "min_periods",
                    "center",
                    "win_type",
                    "on",
                    "axis",
                    "closed",
                    "step",
                    "method",
                ]
            )

        if isinstance(ns.func, str):
            funcs = to_supported_function(ns.func)
            if funcs is None:
                reason = f"unsupported function: {ns.func}"
        elif isinstance(ns.func, (list, tuple)):
            if len(ns.func) == 0:
                raise ValueError("no results")
            reason = "list of function is not supported"

        if reason:
            return self._fallback_call(
                "aggregate", args, kwargs, reason=reason
            )

        window = rolling_ns.window
        funcs = irutils.make_vector_or_scalar_of_str(funcs)
        return DataFrame._create(
            ir.rolling_aggregate(self._obj._value, window, funcs)
        )


class SeriesRolling(Rolling):
    def aggregate(self, *args, **kwargs):
        ns = utils.decode_args(
            args, kwargs, pandas.core.window.rolling.Rolling.aggregate
        )

        rolling_ns = utils.decode_args(
            self._rolling_args, self._rolling_kwargs, pandas.Series.rolling
        )

        if not isinstance(rolling_ns.window, int):
            reason = "window is not int"
        else:
            reason = rolling_ns.is_not_default(
                [
                    "min_periods",
                    "center",
                    "win_type",
                    "on",
                    "axis",
                    "closed",
                    "step",
                    "method",
                ]
            )

        if isinstance(ns.func, str):
            funcs = to_supported_function(ns.func)
            if funcs is None:
                reason = f"unsupported function: {ns.func}"
        elif isinstance(ns.func, (list, tuple)):
            if len(ns.func) == 0:
                raise ValueError("no results")
            reason = "list of function is not supported"

        if reason:
            return self._fallback_call(
                "aggregate", args, kwargs, reason=reason
            )

        window = rolling_ns.window
        funcs = irutils.make_vector_or_scalar_of_str(funcs)
        return Series._create(
            ir.rolling_aggregate(self._obj._value, window, funcs)
        )
