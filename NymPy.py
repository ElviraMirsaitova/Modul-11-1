import numpy as np
import matplotlib.pyplot as plt

arr = np.arange(12)
# print(arr)
# print()
arr = arr.reshape(3,4)
print(arr)
# print()
#print(np.transpose(arr))
# print()
# print(arr)
# print()
# print(arr.reshape(12,))

    #восстановление координат
list3 = [3.17, -1.58, -1.59]
plt.plot(list3)
plt.show()

arr3 = np.array(list3)
arr3 = arr3.reshape(3,1)
print( arr3)

ves = [[0.32], [0.95]]
arr_ves = np.array(ves)
arr_ves = np.transpose(arr_ves)
print(arr_ves)
coordin = np.dot(arr3, arr_ves)
#print(coordin)
list_coord = []
for i in coordin:
    list_coord.append(i)
print(list_coord)