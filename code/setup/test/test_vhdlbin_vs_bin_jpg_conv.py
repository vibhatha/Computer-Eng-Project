import scipy.misc
from numpy import genfromtxt

# vhdl_source_bin_file = 'image_3_200x200_pad.min'
# vhdl_source_bin_path = 'binaries/'

# vhdlapi2 = vhdlapi.VhdlAPI(source_bin_path=vhdl_source_bin_path, source_bin_file=vhdl_source_bin_file)

# vhdlapi2.trimvhdlslds('binaries/sliding/image_3_200x200_pad_slidingwindow__40000x9.sld')
source_file_bin='binaries/v2/crop/pad/image_3_bin_400x400_pad.min'
image_array_bin = genfromtxt(source_file_bin, delimiter=',')
output_file_bin ='test/vhdlvsbinjpgcomp/bin2jpg.jpg'
scipy.misc.imsave(output_file_bin, image_array_bin)

source_file_vhdlbin='binaries/v2/crop/vhdlbin/image_3_bin_400x400_pad.vhdlbin'
image_array_vhdlbin = genfromtxt(source_file_bin, delimiter=',')
output_file_vhdlbin ='test/vhdlvsbinjpgcomp/vhdlbin2jpg.jpg'
scipy.misc.imsave(output_file_vhdlbin, image_array_vhdlbin)
