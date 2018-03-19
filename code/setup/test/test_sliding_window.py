import numpy as np


def sliding_window_test(arr):
    a = arr[0:3,0:3]
    a1 = arr[0:3,1:4]
    a2 = arr[0:3, 2:5]
    b1 = arr[1:4,0:3]
    b2 = arr[1:4, 1:4]
    b3 = arr[1:4, 2:5]
    print(a)
    print(a1)
    print(a2)
    print(arr)
    print(b1)
    print(b2)
    print(b3)


def sliding_window(arr, window_size=3):
    rows = len(arr)
    cols = len(arr[0])
    print(rows,cols)
    sliders = []
    for i in range(0,rows-2):
        for j in range(0,cols-2):
            window = arr[i:i+3,j:j+3]
            print(window)
            window_flat = window.flatten()
            print(window_flat)
            sliders.append(window_flat)

    print(len(sliders),len(sliders[0]))


a = np.array([[0,0,0,0,0],[0,1,2,3,0],[0,4,5,6,0],[0,7,8,9,0], [0,0,0,0,0]])
print(a)

sliding_window(a)


