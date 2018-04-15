from numpy import genfromtxt
import numpy as np


class FilterAPI:

    filter_path = 'filter/'
    filter_file = '8x8_cross.filter'

    def __init__(self, filter_path, filter_file):
        print("Filter Path : " + filter_path)
        print("Filter File : " + filter_file)

    def mat2vec(self):
        file_path = self.filter_path+self.filter_file
        matrix = genfromtxt(file_path, delimiter=',')
        vector = matrix.flatten()
        print("Converted Vector : ")
        print(vector)
        dest_file = str.split(file_path,".")[0]+"_vector.filter"
        np.savetxt(dest_file, vector, delimiter=",")

    def loadFilter(self,file_path):
        print("Loading Filter : " + file_path)
        matrix = genfromtxt(file_path, delimiter=',')
        return matrix

    def sliding_window(self, arr, window_size=3):
        rows = len(arr)
        cols = len(arr[0])
        print(rows, cols)
        sliders = []
        for i in range(0, rows - (window_size-1)):
            for j in range(0, cols - (window_size-1)):
                window = arr[i:i + window_size, j:j + window_size]
                window_flat = window.flatten()
                sliders.append(window_flat)

        return np.array(sliders)

    def save_sliding_window(self, window_size=3, source_file='binaries/image_3_200x200_pad.pad', dest_file='binaries/sliding/file1_slidingwindow'):
        #print("sliding window source file : ",source_file)
        arr = genfromtxt(source_file, delimiter=',')
        new_arr = self.sliding_window(arr, window_size)
        new_arr1 = new_arr
        rows = len(new_arr)
        cols = len(new_arr[0])
        print(rows,cols)
        dest_file = str.split(dest_file,".")[0]+"__"+str(rows)+"x"+str(cols)+".sld"
        dest_file_trim = str.split(dest_file, ".")[0] + "__" + str(rows) + "x" + str(cols) + "_trim.sld"
        #print("Destination Sliding Window File : ",dest_file)
        print(new_arr)
        np.savetxt(dest_file, new_arr, delimiter=",",fmt='%d')
        np.savetxt(dest_file_trim, new_arr1, delimiter='', fmt='%d')
