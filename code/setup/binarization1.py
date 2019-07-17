import matplotlib
import matplotlib.pyplot as plt

from skimage import io
from skimage.data import page
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)
from skimage.filters import threshold_mean

matplotlib.rcParams['font.size'] = 9

io.use_plugin('matplotlib', 'imread')
image = page()
image_base = "images/crop/v5/"
image_file = "image_3_bin_400x400_crop.jpg"
image = io.imread(image_base+image_file)

binary_global = image > threshold_otsu(image)
#binary_global = image > threshold_mean(image)

window_size = 63
thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(image, window_size=window_size)

binary_niblack = image > thresh_niblack
binary_sauvola = image > thresh_sauvola

plt.figure(figsize=(8, 7))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Global Threshold')
plt.imshow(binary_global, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(binary_niblack, cmap=plt.cm.gray)
plt.title('Niblack Threshold')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()
