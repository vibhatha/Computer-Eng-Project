import numpy as np
import ImageAPI as imapi
import FilterAPI as fltapi
import ImageCVAPI as imcv
import VhdlAPI as vhdlapi
import os

filter_path = "filter/"
filter_file = "3x3_cross.filter"

image_base = "images/"
image_file = "image_3.jpg"


fltapi1 = fltapi.FilterAPI(filter_path = filter_path, filter_file = filter_file)
experiment_version ='v3'
experiment_base='binaries/'+experiment_version
output_path4_1 = experiment_base+'/crop'
output_path4_2 = output_path4_1+'/bin/'
output_path4_3='images/crop/'+experiment_version+'/'
step5_dest_path = experiment_base+'/crop/pad/'
step6_output_path_vhdlbin = experiment_base+'/crop/vhdlbin/'
step6_output_path_pad_jpg = 'images/crop/'+experiment_version+'/pad/'
step7_output_path = 'images/crop/'+experiment_version+'/vhdlbin2jpg'
step7_output_path2 = experiment_base+'/crop/sliding'

def step1():
    # Step 1

    base_path = ''
    bin_dir = "binaries"
    image_dir = "images/originals"
    image_urls = []
    image_file_path = "imageurls/imageurls.txt"


    # downloads images from ImageNet Data Sources
    # images/originals have original images
    imapi2 = imapi.ImageAPI(image_file_path, base_path, bin_dir, image_dir)
    imapi2.download_images()

def step2():

    # Step 2
    # Convert Images to Binary Format Using OpenCV
    # Scales the data 0 or 255 roughly.

    image_base = "images/originals/"
    image_file = "image_2.jpg"
    imcv1 = imcv.ImageCVAPI(file_path=image_base, source_file=image_file)
    imcv1.img2bin()

    #binaries filed are moved to images/opencvbinaries



def step3():


    #Step 3
    # Crop the binary image to the needed size

    base_path = ''
    bin_dir = "binaries"
    image_dir = "images"
    image_urls = []
    binary_image_file_path = "imageurls/localimages.txt"

    imapi2 = imapi.ImageAPI(binary_image_file_path, base_path, bin_dir, image_dir)
    image_local_paths = imapi2.load_local_image_urls(binary_image_file_path)
    binary_save_path = experiment_base#'binaries/v2'
    imapi2.img2binary(image_local_paths, binary_save_path)

    #this saves the binary converted image as a binary in binaries/v2 folder


def step4():


    #Step 4

    base_path = ''
    bin_dir = "binaries"
    image_dir = "images"
    image_urls = []
    binary_image_file_path = "imageurls/localimages.txt"


    ## In this step we crop images
    imapi3 = imapi.ImageAPI(binary_image_file_path, base_path, bin_dir, image_dir)
    width=400
    height=400
    imageIds = [0,1,2,3]
    for imageId in imageIds:
        print(imageId)
        source_image=experiment_base+"/image_"+str(imageId)+"_bin.mat"
        imapi3.crop_image(width=width, height=height, source_image=source_image,output_path=output_path4_2)
        source_file=experiment_base+"/crop/bin/image_"+str(imageId)+"_bin"+"_"+str(width)+"x"+str(height)+".min"
        imapi3.csv2jpg(source_file, output_path4_3)

    # This procedure saves binarized crop binary values in binaries/v2/crop/bin folder
    # The jpg version of those converted images are in images/crop/v2/ folder

def step5():
    # Step 5
    base_path = ''
    bin_dir = "binaries"
    image_dir = "images"
    image_urls = []
    binary_image_file_path = "imageurls/localimages.txt"
    imapi4 = imapi.ImageAPI(binary_image_file_path, base_path, bin_dir, image_dir)
    width=400
    height=400
    imageIds = [0,1,2,3]
    pad_width = 1
    for imageId in imageIds:
        source_min_file = experiment_base+"/crop/bin/image_"+str(imageId)+"_bin_"+str(width)+"x"+str(height)+".min"
        imapi4.pad_image(source_min_file, pad_width,imapi4.padwithones,dest_path=step5_dest_path)

    # The binarized images are padded and saved /binaries/v2/crop/pad folder.


def step6():

    # Step 6

    width=400
    height=400
    imageIds = [0,1,2,3]
    pad_width = 1
    vhdl_source_bin_path = experiment_base+'/crop/pad/'

    for imageId in imageIds:
        vhdl_source_bin_file = 'image_'+str(imageId)+'_bin_'+str(width)+'x'+str(height)+'_pad.min'
        vhdlapi2 = vhdlapi.VhdlAPI(source_bin_path=vhdl_source_bin_path, source_bin_file=vhdl_source_bin_file)
        vhdlapi2.bin2vhdl(output_path=step6_output_path_vhdlbin)
        vhdl_bin_source_path = experiment_base+'/crop/pad/image_'+str(imageId)+'_bin_'+str(width)+'x'+str(height)+'_pad.min'
        vhdlapi2.padbin2jpg(vhdl_bin_source_path,step6_output_path_pad_jpg)

    # In this step the vhdl format binary files are being written to binaries/v2/crop/vhdlbin
    # And also the padded images are saved in images/crop/v2/pad/ folder




def step7():
    ## Step 7

    width = 400
    height = 400
    vhdl_source_bin_path = experiment_base+'/crop/pad/'
    imageIds = [0, 2, 3]

    for imageId in imageIds:
        vhdl_source_bin_file = 'image_' + str(imageId) + '_bin_' + str(width) + 'x' + str(height) + '_pad.min'
        vhdlapi3 = vhdlapi.VhdlAPI(source_bin_path=vhdl_source_bin_path, source_bin_file=vhdl_source_bin_file)
        vhdlbin_file_path = experiment_base+'/crop/vhdlbin/image_' + str(imageId) + '_bin_' + str(width) + 'x' + str(
            height) + '_pad.vhdlbin'
        vhdlbin_img2_binimg_path = step7_output_path+'/image_' + str(imageId) + '_' + str(width) + 'x' + str(
            height) + '_pad_rev_vhdlbin.jpg'
        vhdlapi3.vhdlbinimg2binimg(vhdlbin_file_path, vhdlbin_img2_binimg_path)
        vhdlbin_source_file = experiment_base+'/crop/vhdlbin/image_' + str(imageId) + '_bin_' + str(width) + 'x' + str(
            height) + '_pad.vhdlbin'
        print(vhdlbin_source_file)

        slidingwindow_dest_file = step7_output_path2+'/image_' + str(imageId) + '_bin_' + str(width) + 'x' + str(
            height) + '_pad_slidingwindow.sld'
        fltapi1.save_sliding_window(window_size=3, source_file=vhdlbin_source_file, dest_file=slidingwindow_dest_file)

        ##slding_window_source_file = 'binaries/v2/crop/sliding/'+'image_'+str(imageId)+'_bin_'+str(width)+'x'+str(height)+'_pad_slidingwindow__'+str(width*height)+'x9.sld'
        ##print("sliding windows source file : ", slding_window_source_file)
        ##vhdlapi3.trimvhdlslds(slding_window_source_file)

        ## This step saves the load the vhdlbin files and generate sliding window added .sld files

        ## folder binaries/v2/crop/sliding containes the sld files
        ## And also , removed and int casted files with trim extension is in the same folder.


def init():
    base_path_validity = not(os.path.exists(experiment_base))
    step4_path_validity1 = not(os.path.exists(output_path4_1))
    step4_path_validity2 = not(os.path.exists(output_path4_2))
    step4_path_validity3 = not(os.path.exists(output_path4_3))
    step5_dest_path_validity = not(os.path.exists(step5_dest_path))
    step6_output_path_vhdlbin_validity = not(os.path.exists(step6_output_path_vhdlbin))
    step6_output_path_pad_jpg_validity = not(os.path.exists(step6_output_path_pad_jpg))
    step7_output_path_validity = not(os.path.exists(step7_output_path))
    step7_output_path2_validity = not (os.path.exists(step7_output_path2))
    print(base_path_validity)
    print(step4_path_validity1)
    if(base_path_validity):
        os.makedirs(experiment_base)
    if(step4_path_validity1):
        os.makedirs(output_path4_1)
    if (step4_path_validity2):
        os.makedirs(output_path4_2)
    if (step4_path_validity3):
        os.makedirs(output_path4_3)
    if(step5_dest_path_validity):
        os.makedirs(step5_dest_path)
    if(step6_output_path_vhdlbin_validity):
        os.makedirs(step6_output_path_vhdlbin)
    if (step6_output_path_pad_jpg_validity):
        os.makedirs(step6_output_path_pad_jpg)
    if (step7_output_path_validity):
        os.makedirs(step7_output_path)
    if (step7_output_path2_validity):
        os.makedirs(step7_output_path2)


init()
step1()
step2()
step3()
step4()
step5()
step6()
step7()

