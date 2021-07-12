import os
import sys
import cv2 as cv
import numpy as np


file = sys.argv[1]

img = cv.imread(file)

kernel = np.ones((5,5),np.float32)/25
dst = cv.filter2D(img,-1,kernel)
cv.imwrite(file+".filter2d.png",dst)


blur = cv.blur(img,(5,5))
cv.imwrite(file+".blur.png",blur)

gblur = cv.GaussianBlur(img,(5,5),0)
cv.imwrite(file+".gblur.png",gblur)


median = cv.medianBlur(img,5)
cv.imwrite(file+".median.png",gblur)

filterbi = cv.bilateralFilter(img,9,75,75)
cv.imwrite(file+".filterbi.png",filterbi)