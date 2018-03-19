import numpy as np
import ImageAPI as imapi
import FilterAPI as fltapi

base_path = ''
bin_dir = "binaries"
image_dir = "images"
image_urls = []
image_file_path = "imageurls/imageurls.txt"

filter_path = "filter/"
filter_file = "3x3_cross.filter"

imapi = imapi.ImageAPI(image_file_path, base_path, bin_dir, image_dir)

# download_paths = imapi.download_images()
# imapi.load_images(download_paths)

# imapi.binarize_matrix("binaries/image_0.mat")
# imapi.crop_image(width=200, height=200, source_image="binaries/image_0.mat")
# imapi.csv2jpg("binaries/image_0_200x200.min")

# imapi.binarize_matrix("binaries/image_0_200x200.min")

fltapi = fltapi.FilterAPI(filter_path = filter_path, filter_file = filter_file)
fltapi.mat2vec()
filter = fltapi.loadFilter("filter/3x3_cross_vector.filter")
print(filter)

a = np.arange(6)
a = a.reshape(2,3)
print(a)


pad_image = imapi.pad_image("binaries/image_0_10x10.min", 1,imapi.padwithones)
print(pad_image)

imapi.csv2jpg("binaries/image_0_10x10_pad.min")


