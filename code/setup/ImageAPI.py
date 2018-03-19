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


    def crop_image(self, width = 50, height = 50, source_image='', start_pos_x = 100, start_pos_y = 100):
        output_file = str.split(source_image, ".")[0]+"_"+str(height)+"x"+str(width)+ ".min"
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
                print(write_line)
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

    def csv2jpg(self, source_file):
        image_array = genfromtxt(source_file, delimiter=',')
        output_file = str.split(source_file,".")[0]+"_crop.jpg"
        scipy.misc.imsave(output_file, image_array)



