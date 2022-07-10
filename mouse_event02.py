import numpy as np
import cv2
import math
import keyboard

class mouse_event():
    def __init__(self,drawing,firstx,lastx,firsty,lasty,ix,iy):
        self.drawing=drawing

        self.ix=ix
        self.iy=iy
        self.firstx=firstx
        self.lastx=lastx
        self.firsty=firsty
        self.lasty=lasty
    def draw_circle(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True

            self.ix, self.iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:

            if self.drawing == True:
                radius = int(math.sqrt(((self.ix - x) ** 2) + ((self.iy - y) ** 2)))
                cv2.circle(img, (self.ix, self.iy),radius, (255, 0, 0), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing= False
            radius = int(math.sqrt(((self.ix - x) ** 2) + ((self.iy - y) ** 2)))
            cv2.circle(img, (self.ix, self.iy),radius, (255, 0, 0), -1)
    def draw_rect(self,event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True

            self.ix, self.iy = x, y
            self.firstx, self.firsty= x, y
        elif event == cv2.EVENT_MOUSEMOVE:

            if self.drawing == True:

                cv2.rectangle(img, (self.ix, self.iy), (x, y), (255, 0, 0), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing= False

            cv2.rectangle(img, (self.ix, self.iy), (x, y), (255, 0, 0), -1)
            self.lastx, self.lasty= x, y
            cropped = img[self.firstx:self.lastx, self.firsty:self.lasty]
        while (1):
            cv2.imshow('cropped', cropped)
            k = cv2.waitKey(1) & 0xFF
            if k == ord("q"):
                break
            cv2.destroyWindow(cropped)

    def rgb_val(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            red=img[x,y,2]
            green=img[x,y,1]
            blue=img[x,y,0]
            font=cv2.FONT_HERSHEY_SIMPLEX
            strXY=str(red)+","+str(green)+","+str(blue)
            cv2.putText(img,strXY,(x,y),font,1,(255,0,255),2)
            cv2.imshow("image", img)
    def save_img(self,event,x,y,flags,param):
        if event==cv2.EVENT_LBUTTONDOWN:
            cv2.imwrite("npzeros.jpg", img)

    def rotate(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    def paintbrush(self,event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.ix, self.iy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing == True:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False
            cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
    def callback(self):
        cv2.namedWindow('image')
        circleshort="alt+x"
        rectshort="alt+c"
        rgbshort="alt+v"
        saveshort="alt+s"
        rotateshort="alt+r"
        paintbrushshort="alt+b"

        keyboard.add_hotkey(rectshort,lambda:cv2.setMouseCallback('image', self.draw_rect ))
        keyboard.add_hotkey(circleshort,lambda:cv2.setMouseCallback('image', self.draw_circle))
        keyboard.add_hotkey(rgbshort, lambda: cv2.setMouseCallback('image', self.rgb_val))
        keyboard.add_hotkey(saveshort, lambda: cv2.setMouseCallback('image', self.save_img))
        keyboard.add_hotkey(rotateshort, lambda: cv2.setMouseCallback('image', self.rotate))
        keyboard.add_hotkey(paintbrushshort, lambda: cv2.setMouseCallback('image', self.paintbrush))

        while (1):
            cv2.imshow('image', img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
        cv2.destroyAllWindows()

img = np.zeros((512,512,3), np.uint8)
cv2.imwrite("npzeros.jpg", img)
x1=mouse_event(False,0,0,0,0,-1,-1)

x1.callback()