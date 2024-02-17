# Copyright (c) 2012 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/license/zlib

from .__about__  import * ; del __about__  # noqa
from .__config__ import origin

import sys
__import__(origin)

QQt = sys.modules[__name__]

# Utils
from ._emmiter import StreamEmitter
from ._signal  import Signal

# Wrapper for origin.

sys.modules[__name__] = sys.modules[origin]
for name, module in sys.modules.copy().items():
    if name.startswith(origin + "."):
        sys.modules[__name__ + name[len(origin):]] = sys.modules[name]

try:
    import vtkmodules
    from vtkmodules.qt import PyQtImpl
except ImportError:
    PyQtImpl = None
else:
    if PyQtImpl is None:
        # Monkey-patch for vtkmodules.qt (vtk < 9.3.0).
        import importlib
        # Has an implementation has been imported yet?
        for impl in ["PySide6", "PyQt6"]:
            if impl in sys.modules:
                # Sometimes an attempted import can be crufty (e.g., unclean
                # uninstalls of PyQt5), so let's try to import the actual functionality
                try:
                    importlib.import_module(impl + '.QtCore')
                except Exception:
                    pass
                else:
                    sys.modules["vtkmodules.qt"].PyQtImpl = PyQtImpl = impl
                    sys.modules[__name__] = QQt
                    from .vtkmodules.qt import QVTKRenderWindowInteractor as patched
                    sys.modules[__name__] = sys.modules[origin]
                    sys.modules["vtkmodules.qt.QVTKRenderWindowInteractor"] = patched
                    break
        del importlib

sys.modules[origin].StreamEmitter = StreamEmitter
sys.modules[origin].Signal = Signal
