# Copyright (c) 2023 NEC Corporation. All Rights Reserved.

import atexit
import contextlib
import os


class Level:
    # dummy. Updated by init
    NONE = DEFAULT = VERBOSE = DEBUG = None

    @staticmethod
    def from_str(level: str):
        tbl = {
            "0": Level.NONE,
            "1": Level.DEFAULT,
            "2": Level.VERBOSE,
            "3": Level.DEBUG,
            "None": Level.NONE,
            "Default": Level.DEFAULT,
            "Verbose": Level.VERBOSE,
            "Debug": Level.DEBUG,
        }
        return tbl.get(level, Level.DEBUG)


def enable_tracing(level):
    raise RuntimeError("firefw.tracing was used before initialization")


class TracingScope:
    def __init__(self, level, message: str):
        pass

    def pop(self):
        pass


@contextlib.contextmanager
def scope(level, message):
    s = TracingScope(level, message)
    try:
        yield s
    finally:
        s.pop()


def start_tracing_if_enabled(level):
    if level is not None:
        env = "TEST_UNDECLARED_OUTPUTS_DIR"
        d = os.environ.get(env)

        # Let chome_tracing_sink store to "trace.json" in current directory.
        if d is None:
            os.environ[env] = "."

        enable_tracing(Level.from_str(level))
        scope = TracingScope(Level.DEFAULT, "top")

        def finalize():
            scope.pop()
            disable_tracing()

        atexit.register(finalize)


def init(ext):
    """
    fire.tracing has to be initialized with the extension which provides
    underlying tracing interface.
    """
    global Level
    global enable_tracing
    global disable_tracing
    global TracingScope

    Level.NONE = ext.TracingLevel.NONE
    Level.DEFAULT = ext.TracingLevel.Default
    Level.VERBOSE = ext.TracingLevel.Verbose
    Level.DEBUG = ext.TracingLevel.Debug

    enable_tracing = ext.enable_tracing
    disable_tracing = ext.disable_tracing

    class TracingScope:
        def __init__(self, level, message: str):
            self.cscope = ext.push_tracing_scope(level, message)

        def pop(self):
            ext.pop_tracing_scope(self.cscope)
