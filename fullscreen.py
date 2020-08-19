import cv2
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

        img_dummy = cv2.resize(0, (self.width, self.height)) #zero padding image
        self.imshow(img_dummy)
        cv2.waitKey(100)

    def imshow(self, image):
        if image.shape[0]!=self.height or image.shape[1]!=self.width:
            image = cv2.resize(image, (self.width, self.height), interpolation=cv2.INTER_NEAREST)
        cv2.imshow(self.name, image)

    def destroyWindow(self):
        cv2.destroyWindow(self.name)

def main():
    import numpy as np
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=str, default=None, help="Image file path")
    parser.add_argument("-i", "--id", type=int, default=0, help="Monitor ID")
    args = parser.parse_args()

    monitor_id = args.id
    win = FullScreen(monitor_id)

    width = win.width
    height = win.height

    img_from_file = cv2.imread(args.file)
    if img_from_file is not None:
        image = cv2.resize(img_from_file, (width, height)) 
    else:
        image = np.fromfunction(lambda y, x, c: x/width*255*(c==1)+y/height*255*(c==2), (height, width, 3)).astype(np.uint8)

    win.imshow(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
