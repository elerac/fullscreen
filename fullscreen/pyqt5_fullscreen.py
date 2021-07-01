"""
Caution! This fullscreen program using PyQt5 is really TRICKY.

This program consists of two modules, 
(1) fullscreen app (main funtion) and 
(2) launching and managing class for the fullscreen app (FullScreen class).
"""
import os
import sys
import argparse
import threading
import subprocess
import importlib

import numpy as np
from PyQt5 import QtWidgets, QtGui

is_pillow_available = importlib.util.find_spec("PIL") is not None
if is_pillow_available:
    from PIL import Image
else:
    import cv2

def imwrite(filename, image):
    if is_pillow_available:
        if image.ndim == 2:
            img_rgb = np.dstack([image]*3) # Gray -> RGB
        else:
            img_rgb = image[:, :, ::-1] # BGR -> RGB
        pil_img = Image.fromarray(img_rgb)
        pil_img.save(filename)
    else:
        cv2.imwrite(filename, image)

class FullScreen:
    """Full-screen with PyQt5 backend
    """
    __tmp_filename = "tmp_pyqt5_fullscreen.png"

    def __init__(self):
        app = QtWidgets.QApplication([])
        screen = app.primaryScreen()
        size = screen.size()
        self.width = size.width()
        self.height = size.height()
    
    @property
    def shape(self):
        return self.height, self.width, 3
    
    def imshow(self, image):
        self.destroyWindow()
        
        imwrite(self.__tmp_filename, image)

        processThread = threading.Thread(target=self._launch_fullscreen_app)
        processThread.start()
    
    def _launch_fullscreen_app(self):
        python_bin = sys.executable
        py_filename = __file__
        tmp_filename = self.__tmp_filename

        cmd = f"{python_bin} {py_filename} {tmp_filename}"
        self._p = subprocess.Popen(cmd, shell=True)
    
    def destroyWindow(self):
        if hasattr(self, "_p"):
            self._p.kill()

    def __del__(self):
        self.destroyWindow()
        os.remove(self.__tmp_filename)

def main():
    """Fullscreen app
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    args = parser.parse_args()
    
    app = QtWidgets.QApplication([])
    
    widget = QtWidgets.QLabel()
    widget.showFullScreen()
    
    qt_img = QtGui.QImage(args.filename)
    widget.setPixmap(QtGui.QPixmap.fromImage(qt_img))

    widget.update()

    sys.exit(app.exec_())

if __name__=="__main__":
    main()
