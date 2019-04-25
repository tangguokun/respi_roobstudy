import cv2
import play
import numpy as np
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(392,227),1,(55,255,155),70)
        cv2.circle(img,(332,227),1,(55,255,155),70)
        cv2.imshow("image",img)
        cv2.waitKey(1)
        play.play()


cv2.namedWindow('image')
img=cv2.imread("timg.jpg")
cv2.circle(img,(392,227),30,(55,255,155),8)
cv2.circle(img,(332,227),30,(55,255,155),8)
image=img.copy()
cv2.setMouseCallback('image',draw_circle)

def dian():
    while(1):
        cv2.imshow("image",image)
        if cv2.waitKey(100) & 0xFF==ord("q"):
            cv2.destroyAllWindows()
            break

dian()
