from numpy import genfromtxt
import numpy as np

class FilterAPI:
    filter_path='filter/'
    filter_file='3x3_cross.filter'

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


