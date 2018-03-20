import cv2

img = cv2.imread("test/cat_200.png", 0)
ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)
cv2.imshow('Binary Image', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('test/cat_binarizecv2.jpg', thresh_img)
