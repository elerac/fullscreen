def FullScreen(backend="tkinter", **kwargs):
    """Provide FullScreen instance
    """
    if backend == "tkinter":
        from . import tkinter_fullscreen
        return tkinter_fullscreen.FullScreen()
    elif backend == "cv2":
        from . import cv2_fullscreen
        return cv2_fullscreen.FullScreen(**kwargs)
    else:
        return None
