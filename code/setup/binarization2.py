import cv2
import numpy as np
from matplotlib import pyplot as plt
import ImageAPI as imapi

image_base = "images/crop/v5/"
image_file = "image_3_bin_400x400_crop.jpg"
img = cv2.imread(image_base+image_file, 0)

ret, imgf = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

ret, imgf2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

ret, imgf3 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

# blur = cv2.GaussianBlur(img, (5,5), 0)
# ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

plt.subplot(3, 1, 1), plt.imshow(img, cmap='gray')
plt.title('Original Noisy Image'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 1, 2), plt.hist(img.ravel(), 256)
plt.axvline(x=ret, color='r', linestyle='dashed', linewidth=2)
plt.title('Histogram'), plt.xticks([]), plt.yticks([])
plt.subplot(3, 1, 3), plt.imshow(imgf, cmap='gray')
plt.title('Otsu thresholding'), plt.xticks([]), plt.yticks([])
plt.show()

imgf = imgf3-imgf2
exp="otsu-binary-otsu"
cv2.imwrite("binaries/test/"+exp+".jpg", imgf)

binary_image_file_path="binaries/test/otsu.jpg"
base_path = "binaries/test"
bin_dir = "binaries/test/"+exp+".txt"
image_dir="binaries/test"
experiment_base = image_dir
np.savetxt(bin_dir, imgf, delimiter=',', fmt='%d')
