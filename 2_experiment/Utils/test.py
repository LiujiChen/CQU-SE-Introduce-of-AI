import cv2

img = cv2.imread('../Data/data.png')
image_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('test', img)
cv2.imshow('grey', image_grey)
cv2.waitKey()