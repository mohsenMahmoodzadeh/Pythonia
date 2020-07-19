import cv2 as cv
import numpy as np

src = cv.imread('./img.jpg')
out = src

blue = src[:,:,0]
green = src[:,:,1]
red = src[:,:,2]

blue_thresh, blue_thr_img = cv.threshold(blue,0, 255,cv.THRESH_BINARY + cv.THRESH_OTSU)
green_thresh, green_thr_img = cv.threshold(green,0, 255,cv.THRESH_BINARY + cv.THRESH_OTSU)
red_thresh, red_thr_img = cv.threshold(red,0, 255,cv.THRESH_BINARY + cv.THRESH_OTSU)

# threshold = np.where((src[:,:,0] > 255 - int(blue_thresh)) & (src[:,:,1] > 255 - int(green_thresh)) & (src[:,:,2] > 255 - int(red_thresh)))
threshold = np.where((src[:,:,0] > 200) & (src[:,:,1] > 200) & (src[:,:,2] > 200))

out[threshold] = (255,255,0)

cv.imshow('out', out)
cv.waitKey(0)
cv.imwrite('./output.jpg', out)
