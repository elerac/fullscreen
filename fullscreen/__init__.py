def FullScreen(backend="tkinter", **kwargs):
    """Provide FullScreen instance
    """
    if backend == "tkinter":
        from . import tkinter_fullscreen
        return tkinter_fullscreen.FullScreen()
    elif backend == "cv2":
        from . import cv2_fullscreen
        return cv2_fullscreen.FullScreen(**kwargs)
    elif backend == "PyQt5":
        from . import pyqt5_fullscreen
        return pyqt5_fullscreen.FullScreen()
    else:
        return None
