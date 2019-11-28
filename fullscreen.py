import cv2
import numpy as np
import screeninfo
import os

class FullScreen:
    def __init__(self, monitor_id):
        self.monitor = screeninfo.get_monitors()[monitor_id]
        self.width = self.monitor.width
        self.height = self.monitor.height
        self.x = self.monitor.x
        self.y = self.monitor.y
        self.name = str(monitor_id)
        
        cv2.namedWindow(self.name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(self.name, self.x, self.y)
        cv2.setWindowProperty(self.name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        #Foce the image window to appear on top (MacOS only)
        if os.name == "posix":
            import subprocess
            subprocess.call(["/usr/bin/osascript", "-e", 'tell app "Finder" to set frontmost of process "Python" to true'])

        img_dummy = np.zeros((self.height, self.width), dtype=np.uint8)
        self.imshow(img_dummy)
        cv2.waitKey(1)

    def imshow(self, image):
        if image.shape[0]!=self.height or image.shape[1]!=self.width:
            image = cv2.resize(image, (self.width, self.height), interpolation=cv2.INTER_NEAREST)
        cv2.imshow(self.name, image)

    def destroyWindow(self):
        cv2.destroyWindow(self.name)

def main():
    monitor_id = 0
    win = FullScreen(monitor_id)

    width = win.width
    height = win.height

    image = np.fromfunction(lambda y, x, c: x/width*255*(c==1)+y/height*255*(c==2), (height, width, 3)).astype(np.uint8)

    win.imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
