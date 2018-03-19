import numpy as np
import ImageCVAPI as imcv
import ImageAPI as imapi
import FilterAPI as filapi
from numpy import genfromtxt
import scipy


class VhdlAPI:
    source_bin_file = 'image_0_200x200_pad.min'
    source_bin_path='binaries/'

    def __init__(self, source_bin_path = source_bin_path, source_bin_file = source_bin_file):
        self.source_bin_path = source_bin_path
        self.source_bin_file = source_bin_file

    def bin2vhdl(self):
        source_file = self.source_bin_path + self.source_bin_file
        output_file = self.source_bin_path + str.split(self.source_bin_file,".")[0]+".vhdlbin"
        print('Converting to VHDL Binary Format')
        array = genfromtxt(source_file, delimiter=',')
        print(array)
        array[array == 255.0] = 1
        print(array)
        np.savetxt(output_file, array, delimiter=",")

    def vhdlbin2jpg(self,bin_file):
        image_array = genfromtxt(bin_file, delimiter=',')
        output_file = str.split(bin_file, ".")[0] + "_vhdl_crop.jpg"
        scipy.misc.imsave(output_file, image_array)
