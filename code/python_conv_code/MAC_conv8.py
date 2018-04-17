import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.misc


def change_array(array):
        rows = len(array)
        cols = len(array[0])
        for i in range(0,rows):
            for j in range(0,cols):
                val = array[i][j]
                if(val==0):
                    array[i][j] = 255
                else:
                    array[i][j] = 0
        return array
    
def conv(filter,array):
        output1 = []
        rows = len(array)
        cols = len(array[0])
        for i in range(0,rows):
            count = 0
            for j in range(0,cols): 
                count=count+ array[i][j]*filter[j]
            if(count>0):
                count=1
            else:
                count=0  
            output1.append(count)
        return output1

filterSize=8
vhdl_output_bin_file = 'output'+str(filterSize)+'x'+str(filterSize)+'.txt'
size=395
inputImagevd = np.loadtxt(vhdl_output_bin_file)
inputImage1 = np.reshape(inputImagevd, (size, size))
plt.imshow(inputImage1, cmap = plt.get_cmap('gray'))
#plt.show()


input_bin_file = 'input_mac'+str(filterSize)+'x'+str(filterSize)+'.txt'
filter_bin_file = 'filter_mac'+str(filterSize)+'x'+str(filterSize)+'.txt'
output_bin_file = 'output_mac'+str(filterSize)+'x'+str(filterSize)+'.txt'


inputImage2read = np.loadtxt(input_bin_file, delimiter=',')
inputFilter = np.loadtxt(filter_bin_file)

inputImage2read[inputImage2read==0] =-1
inputFilter[inputFilter==0] =-1

ar1 = np.array(conv(inputFilter,inputImage2read))

np.savetxt(output_bin_file, ar1, delimiter="", fmt='%d')

inputImage2 = np.reshape(ar1, (size, size))

plt.imshow(inputImage2, cmap = plt.get_cmap('gray'))
#plt.show()

#check array_equal
print("comparing 3x3 image outputs : " + str(np.array_equal(inputImage1, inputImage2)))

scipy.misc.imsave('image1_'+str(filterSize)+'x'+str(filterSize)+'.jpg', inputImage1)
scipy.misc.imsave('image2_'+str(filterSize)+'x'+str(filterSize)+'.jpg', inputImage2)