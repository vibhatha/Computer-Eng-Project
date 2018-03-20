import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import TestVhdlAPI as vhdlapi

img = mpimg.imread('test/cat_binarizecv2.jpg')

plt.imshow(img, cmap=plt.get_cmap('gray'))
plt.show()
np.savetxt('test/cat_binarized.csv', img, delimiter=",")

source_bin_file = 'cat_binarized.csv'
source_bin_path = 'test/'

vhdlapi1 = vhdlapi.VhdlAPI(source_bin_path=source_bin_path, source_bin_file=source_bin_file)
vhdlapi1.bin2vhdl()
vhdlapi1.vhdlbinimg2binimg( 'test/cat_binarized.vhdlbin', 'test/cat_vhdlbin_img.png')
vhdlapi1.vhdlbin2jpg('test/cat_binarized.vhdlbin')
