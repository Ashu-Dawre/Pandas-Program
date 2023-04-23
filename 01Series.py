import numpy
import pandas

lst=['england','java','microsoft','python','oracle','sql','ethan']
#lst=[9,13,1,45,89,'python',125,75,17,'java',23]

arr=numpy.array(lst)
#print(arr)

print('creating series in pandas')
ser=pandas.Series(arr)
print(ser)
print(ser[3])

