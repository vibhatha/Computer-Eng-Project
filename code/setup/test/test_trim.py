# import urllib.request
import numpy as np
#print('Beginning file download with urllib2...')

#url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
#urllib.request.urlretrieve(url, 'test/cat.jpg')
arr = np.array([[0,0,0,0,0,0],[0,1,2,3,4,0], [0,5,6,7,8,0], [0,9,10,11,12,0],[0,13,14,15,16,0],[0,0,0,0,0,0]])
row_size = len(arr[0])
print(row_size)
a1 = np.delete(arr,0, axis=1)
print(a1)
a2 = np.delete(a1,0,axis=0)
print(a2)
a3 = np.delete(a2,row_size-2,axis=0)
print(a3)
a4 = np.delete(a3,row_size-2,axis=1)
print(a4)
