import urllib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
