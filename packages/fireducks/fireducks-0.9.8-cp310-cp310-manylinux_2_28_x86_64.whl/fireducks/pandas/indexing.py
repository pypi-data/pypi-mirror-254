# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

import logging

import fireducks.core
import fireducks.pandas.utils as utils
from fireducks import ir
from fireducks.irutils import _is_str_list

logger = logging.getLogger(__name__)


class _Indexer:
    def __init__(self, obj, name):
        self.obj = obj
        self.name = name

    def _unwrap(self, reason=None):
        return getattr(self.obj._unwrap(reason=reason), self.name)

    def __getitem__(self, key):
        reason = "fallback _Indexer(" + self.name + ").__getitem__"
        return utils.fallback_call(
            self._unwrap, "__getitem__", key, __fireducks_reason=reason
        )

    def __setitem__(self, key, value):
        reason = "fallback _Indexer(" + self.name + ").__setitem__"
        utils.fallback_call(
            self._unwrap, "__setitem__", key, value, __fireducks_reason=reason
        )
        self.obj._rebind_to_cache()


def is_column_locator(obj):
    if isinstance(obj, str):
        return True
    if _is_str_list(obj):
        return True
    return False


def is_full_slice(slobj):
    return slobj.start is None and slobj.stop is None and slobj.step is None


class _LocIndexer(_Indexer):
    def __init__(self, obj):
        super().__init__(obj, "loc")

    def __getitem__(self, key):
        from fireducks.pandas.series import Series

        t_cls = self.obj.__class__

        if isinstance(key, Series):
            dtype = utils._deduce_dtype(key)
            if dtype is not None and dtype == bool:
                return t_cls._create(ir.filter(self.obj._value, key._value))

        if isinstance(key, tuple) and len(key) == 2:
            r, c = key
            # get column
            if isinstance(r, slice) and is_column_locator(c):
                if is_full_slice(r):  # e.g., loc[:, ['a', 'b']]
                    return self.obj[c]

            if isinstance(r, Series):
                supported_c = True
                if is_column_locator(c):
                    projected = self.obj[c]
                elif isinstance(c, slice) and is_full_slice(c):
                    # TODO: support column slicing
                    projected = self.obj
                else:
                    supported_c = False

                if supported_c:
                    dtype = utils._deduce_dtype(r)
                    if dtype is not None and dtype == bool:
                        return projected.__class__._create(
                            ir.filter(projected._value, r._value)
                        )
                    else:  # TODO: support index selection
                        return _LocIndexer(projected)[r]

            if isinstance(r, slice) and isinstance(c, slice):
                if is_full_slice(r) and is_full_slice(c):  # e.g., loc[:, :]
                    return self.obj

            # get single element
            if isinstance(r, int) and isinstance(c, str):
                if (
                    fireducks.core.get_fireducks_options().fast_fallback
                    and self.obj._fireducks_meta.is_cached()
                ):
                    cache = self.obj._fireducks_meta.get_cache()
                    return cache.loc[key]

        reason = "fallback _LocIndexer(" + self.name + ").__getitem__"
        return utils.fallback_call(
            self._unwrap, "__getitem__", key, __fireducks_reason=reason
        )


class _IlocIndexer(_Indexer):
    def __init__(self, obj):
        super().__init__(obj, "iloc")

    def __getitem__(self, key):
        from fireducks.pandas.series import Series
        from fireducks.pandas.generic import _Scalar

        if isinstance(self.obj, Series) and isinstance(key, int):
            # get single element
            if (
                fireducks.core.get_fireducks_options().fast_fallback
                and self.obj._fireducks_meta.is_cached()
            ):  # read from cache
                cache = self.obj._fireducks_meta.get_cache()
                return cache.iloc[key]
            else:
                value = ir.iloc_scalar(self.obj._value, key)
                return _Scalar(value)._unwrap()

        # self.obj must be DataFrame
        if isinstance(key, tuple) and len(key) == 2:
            r, c = key
            # get single element
            if isinstance(r, int) and isinstance(c, int):
                if (
                    fireducks.core.get_fireducks_options().fast_fallback
                    and self.obj._fireducks_meta.is_cached()
                ):  # read from cache
                    cache = self.obj._fireducks_meta.get_cache()
                    return cache.iloc[key]
                else:
                    columns = self.obj.columns
                    projected = self.obj[columns[c]]
                    value = ir.iloc_scalar(projected._value, r)
                    return _Scalar(value)._unwrap()

            # projection
            if isinstance(r, slice) and isinstance(c, slice):
                if is_full_slice(r):
                    # e.g., iloc[:, :]
                    if is_full_slice(c):
                        return self.obj
                    # e.g., iloc[:, :2]
                    else:
                        columns = self.obj.columns
                        return self.obj[columns[c]]

        reason = "fallback _ILocIndexer(" + self.name + ").__getitem__"
        return utils.fallback_call(
            self._unwrap, "__getitem__", key, __fireducks_reason=reason
        )
