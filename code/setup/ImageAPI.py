import urllib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc
from numpy import genfromtxt

class ImageAPI:
    image_urls = []
    base_path = ''
    bin_dir = ''
    image_dir= ''
    image_file_path = ''

    def __init__(self, image_file_path, base_path, bin_dir, image_dir):
        self.image_urls = self.load_image_urls(image_file_path)
        self.base_path = base_path
        self.bin_dir = bin_dir
        self.image_dir = image_dir

    def load_image_urls(self, image_file_path):
        image_urls = []
        print("Image Url File : " + image_file_path)
        lines = open(image_file_path, "r")
        for line in lines:
            image_urls.append(line)
        self.image_urls = image_urls
        return self.image_urls

    def load_local_image_urls(self,image_file_path):
        image_urls = []
        print("Image Url File : " + image_file_path)
        lines = open(image_file_path, "r")
        for line in lines:
            line = str.split(line,"\n")[0]
            image_urls.append(line)
            image_urls = image_urls
        return image_urls

    def download_images(self):
        download_paths = []
        print("Downloading " + str(len(self.image_urls)) + " images ...")
        count = 0
        for image_url in self.image_urls:
            print(image_url)
            dest_path = str(self.image_dir+"/"+"image_"+str(count)+".jpg")
            print("Downloaded " + dest_path)
            urllib.urlretrieve(image_url, dest_path)
            count = count + 1
            download_paths.append(dest_path)
        return download_paths

    def rgb2gray(self,rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

    def load_images(self, download_paths):
        for image in download_paths:
            print(image)
            img = mpimg.imread(image)
            gray = self.rgb2gray(img)
            # plt.imshow(gray, cmap=plt.get_cmap('gray'))
            # plt.show()
            print(gray.shape)
            print(gray)
            bin_path = self.bin_dir + "/" + str.split(str.split(image,"/")[1],".")[0]+".mat"
            open(bin_path,"w")
            print(bin_path)
            np.savetxt(bin_path, gray, delimiter=',')


    def load_images_local(self, download_paths):
        for image in download_paths:
            print(image)
            img = mpimg.imread(image)
            gray = img
            # plt.imshow(gray, cmap=plt.get_cmap('gray'))
            # plt.show()
            print(gray.shape)
            print(gray)
            bin_path = self.bin_dir + "/" + str.split(str.split(image,"/")[1],".")[0]+".mat"
            open(bin_path,"w")
            print(bin_path)
            np.savetxt(bin_path, gray, delimiter=',')


    def img2binary(self, download_paths, output_path):
        for image in download_paths:
            print(image)
            img = mpimg.imread(image)
            gray = img
            # plt.imshow(gray, cmap=plt.get_cmap('gray'))
            # plt.show()
            print(gray.shape)
            print(gray)
            fnames = (str.split(image,"/"))
            print(fnames)
            bin_path = output_path + "/" + str.split(str.split(image,"/")[2],".")[0]+".mat"
            open(bin_path,"w")
            print(bin_path)
            np.savetxt(bin_path, gray, delimiter=',', fmt='%d')


    def crop_image(self, width = 50, height = 50, source_image='', start_pos_x = 0, start_pos_y = 0, output_path=''):
        fnames = str.split(source_image, ".")
        file_name = str.split(fnames[0],"/")[2]
        print(file_name)
        output_file = output_path+file_name+"_"+str(width)+"x"+str(height)+".min"
        source_content = open(source_image, "r")
        output_file_writer = open(output_file, "w")
        row_count = 0
        myList = []
        for line in source_content:
            myList.append(line)
        for item in myList:
            if(row_count >= start_pos_y and row_count < start_pos_y + height):
                elements = str.split(item,",")
                write_line =''
                y = start_pos_x + width
                x = start_pos_x
                count = 0
                for i in range(x, y):
                    if(count < width -1):
                        write_line = write_line + elements[i] + ","
                    else:
                        write_line = write_line + elements[i] + "\n"
                    count = count + 1
                #print(write_line)
                output_file_writer.write(write_line)
            row_count = row_count + 1

    def binarize_matrix(self, source_file):
        output_file = str.split(source_file,".")[0]+".bin"
        print("Loading file : " + output_file)
        source_content = open(source_file, "r")
        print(source_content)
        myList = []
        for line in source_content:
            myList.append(line)

        for item in myList:
            elements = str.split(item,",")
            size = len(elements)
            for i in range(0, size):
                value = float(elements[i])
                if(value==0):
                    print(value,elements[i])

    def csv2jpg(self, source_file, output_path):
        image_array = genfromtxt(source_file, delimiter=',')
        fnames = str.split(source_file,".")
        print(fnames)
        file_name = str.split(fnames[0],"/")[4]
        output_file = output_path+file_name+"_crop.jpg"
        scipy.misc.imsave(output_file, image_array)

    def padwithones(self,matrix, pad_width, iaxis, kwargs):
        matrix[:pad_width[0]] = 1
        matrix[-pad_width[1]:] = 1
        return matrix

    def padwithzeros(self, matrix, pad_width, iaxis, kwargs):
        matrix[:pad_width[0]] = 0
        matrix[-pad_width[1]:] = 0
        return matrix

    def pad_array(self, array, pad_width, padwidthones):
        padarr = np.lib.pad(array, pad_width, padwidthones)
        print(padarr)

    def pad_image(self, source_file, pad_width, padwidthones, dest_path=''):
        image_array = genfromtxt(source_file, delimiter=',')
        print(source_file)
        print("image_arr",image_array.shape)
        pad_image_array = np.lib.pad(image_array, pad_width, padwidthones)
        print("pad_arr",pad_image_array.shape)
        fnames = source_file.split(".")
        # print(fnames)
        file_name = str.split(fnames[0],"/")[4]
        dest_file = dest_path+file_name+"_pad."+source_file.split(".")[1]
        np.savetxt(dest_file, pad_image_array, delimiter=",", fmt='%d')
        return pad_image_array
