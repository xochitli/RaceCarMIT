import numpy as np
import cv2
img=cv2.imread('c:\\users\\lenovo\\desktop\\bjork.jpg',0)
cv2.imshow('Bjork',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'): 
    cv2.imwrite('deepgray.jpg', img)
    cv2.destroyAllWindows()