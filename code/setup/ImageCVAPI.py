import cv2
import numpy as np

class ImageCVAPI:

    file_path = "images/"
    source_file = "image_0.jpg"

    def __init__(self, file_path = file_path, source_file = source_file):
        self.file_path = file_path
        self.source_file = source_file

    def load_image(self):
        file = self.file_path + self.source_file
        img = cv2.imread(file,0)
        #cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        #cv2.imshow('image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def img2bin(self):
        file = self.file_path + self.source_file
        dest_file = self.file_path + str.split(self.source_file,".")[0]+"_bin.jpg"
        img = cv2.imread(file, 0)
        ret, thresh_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        #cv2.namedWindow('Binary Image', cv2.WINDOW_NORMAL)
        #cv2.imshow('Binary Image', thresh_img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        cv2.imwrite(dest_file, thresh_img)
