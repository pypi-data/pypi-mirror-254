# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

"""FireDucks: DataFrame with Compiler
"""
import os

env = os.environ.get("FIREDUCKS_DISABLE")
if env is None:
    # fireducks_ext.so depends on arrow's shared libraries such as libarrow.so
    # and libarrow_python.so. To load the libraries bundled in pyarrow python
    # module in virtualenv without trying to load system-wide libraries, pyarrow
    # is imported here before importing fireducks_ext.so. See GT #1066 for
    # details.
    import pyarrow
    import pyarrow.acero  # noqa
    import pyarrow.dataset  # noqa

    from fireducks.core import get_fireducks_options

    import fireducks.fireducks_ext.tracing
    from firefw import tracing

    tracing.init(fireducks.fireducks_ext.tracing)
    tracing.start_tracing_if_enabled(get_fireducks_options().trace_level)

    from fireducks.log import get_log_system  # noqa

    from fireducks._version import get_version, get_dfkl_version

    __version__ = get_version()
    __dfkl_version__ = get_dfkl_version()
