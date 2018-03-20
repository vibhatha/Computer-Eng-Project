import numpy as np
import ImageAPI as imapi
import FilterAPI as fltapi
import ImageCVAPI as imcv
import VhdlAPI as vhdlapi

base_path = ''
bin_dir = "binaries"
image_dir = "images"
image_urls = []
image_file_path = "imageurls/imageurls.txt"

filter_path = "filter/"
filter_file = "3x3_cross.filter"

image_base = "images/"
image_file = "image_3.jpg"

imapi1 = imapi.ImageAPI(image_file_path, base_path, bin_dir, image_dir)

# download_paths = imapi.download_images()
# print(download_paths)
# imapi1.load_images(download_paths)

# imapi1.binarize_matrix("binaries/image_0.mat")
# imapi1.crop_image(width=200, height=200, source_image="binaries/image_0.mat")
# imapi1.csv2jpg("binaries/image_0_200x200.min")

# imapi.binarize_matrix("binaries/image_0_200x200.min")

fltapi1 = fltapi.FilterAPI(filter_path = filter_path, filter_file = filter_file)
# fltapi1.mat2vec()
# filter = fltapi1.loadFilter("filter/3x3_cross_vector.filter")
# print(filter)

# a = np.arange(6)
# a = a.reshape(2,3)
# print(a)


# pad_image = imapi1.pad_image("binaries/image_0_10x10.min", 1,imapi.padwithones)
# print(pad_image)

# imapi1.csv2jpg("binaries/image_0_10x10_pad.min")

imcv1 = imcv.ImageCVAPI(file_path=image_base, source_file=image_file)

# imcv1.img2bin()

#imapi1.load_images_local()
base_path = ''
bin_dir = "binaries"
image_dir = "images"
image_urls = []
binary_image_file_path = "imageurls/localimages.txt"
imapi2 = imapi.ImageAPI(binary_image_file_path, base_path, bin_dir, image_dir)
# download_paths = imapi2.download_images()
# imapi2.load_images_local(download_paths)
# imapi2.crop_image(width=200, height=200, source_image="binaries/image_3.mat")
# imapi2.csv2jpg("binaries/image_3_200x200.min")
imapi2.pad_image("binaries/image_3_200x200.min", 1,imapi2.padwithones)

vhdl_source_bin_file = 'image_3_200x200_pad.min'
vhdl_source_bin_path = 'binaries/'

vhdlapi2 = vhdlapi.VhdlAPI(source_bin_path=vhdl_source_bin_path, source_bin_file=vhdl_source_bin_file)

vhdlapi2.bin2vhdl()

# vhdlapi2.vhdlbin2jpg('binaries/image_3_200x200_pad.vhdlbin')

vhdlapi2.vhdlbinimg2binimg('binaries/image_3_200x200_pad.vhdlbin','images/ice_format/image_3_200x200_rev_vhdlbin.jpg')

fltapi1.save_sliding_window(window_size=3, source_file='binaries/image_3_200x200_pad.vhdlbin', dest_file='binaries/sliding/image_3_200x200_pad_slidingwindow.sld')

