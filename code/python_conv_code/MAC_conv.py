import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
    
def conv(array):
        filter1 = np.array([-1, 1, -1, 1, 1, 1, -1, 1, -1])
        output1 = []
        rows = len(array)
        cols = len(array[0])
        for i in range(0,rows):
            count = 0
            for j in range(0,cols): 
                count=count+ array[i][j]*filter1[j]
            if(count>0):
                count=1
            else:
                count=0  
            output1.append(count)
        return output1


vhdl_output_bin_file = 'output.txt'

inputImagevd = np.loadtxt(vhdl_output_bin_file)
inputImage1 = np.reshape(inputImagevd, (400, 400))
plt.imshow(inputImage1, cmap = plt.get_cmap('gray'))
plt.show()


vhdl_input_bin_file = 'input_mac.txt'
vhdl_output_bin_file = 'output_mac.txt'

inputImage2read = np.loadtxt(vhdl_input_bin_file)

inputImage2read[inputImage2read==0] =-1
ar1 = np.array(conv(inputImage2read))

np.savetxt(vhdl_output_bin_file, ar1, delimiter="", fmt='%d')

inputImage2 = np.reshape(ar1, (400, 400))

plt.imshow(inputImage2, cmap = plt.get_cmap('gray'))
plt.show()

#check array_equal
print(np.array_equal(inputImage1, inputImage2))