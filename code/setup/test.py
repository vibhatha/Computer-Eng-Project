import VhdlAPI as vhdlapi


vhdl_source_bin_file = 'image_3_200x200_pad.min'
vhdl_source_bin_path = 'binaries/'

vhdlapi2 = vhdlapi.VhdlAPI(source_bin_path=vhdl_source_bin_path, source_bin_file=vhdl_source_bin_file)

vhdlapi2.trimvhdlslds('binaries/sliding/image_3_200x200_pad_slidingwindow__40000x9.sld')
