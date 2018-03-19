from numpy import genfromtxt
import numpy as np


class FilterAPI:

    filter_path = 'filter/'
    filter_file = '3x3_cross.filter'

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
        for i in range(0, rows - 2):
            for j in range(0, cols - 2):
                window = arr[i:i + window_size, j:j + window_size]
                window_flat = window.flatten()
                sliders.append(window_flat)

        return np.array(sliders)

    def save_sliding_window(self, window_size=3, source_file='binaries/image_3_200x200_pad.vhdlbin', dest_file='binaries/sliding/file1_slidingwindow'):
        arr = genfromtxt(source_file, delimiter=',')
        new_arr = self.sliding_window(arr, window_size)
        rows = len(new_arr)
        cols = len(new_arr[0])
        dest_file = str.split(dest_file,".")[0]+"__"+str(rows)+"x"+str(cols)+".sld"
        np.savetxt(dest_file, new_arr, delimiter=",")
