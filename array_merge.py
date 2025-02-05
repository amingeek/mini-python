import numpy as np

def sum_array(a1):
    merge = ''
    if a1.shape == ():
        return a1
    elif len(a1.shape) == 1:
        for i in a1:
            merge += str(i)
    elif len(a1.shape) == 2:
        for i in a1:
            for j in i:
                merge += str(j)  
    elif len(a1.shape) == 3:
        for i in a1:
            for j in i:
                for k in j:
                    merge += str(k)
    return merge

a1 = np.array([[1, 2, 3, 'a', 'b', 'c'], [4, 5, 6, 7, '8', '9'],[10, 11, 12, 13, 14, 15]])

print(sum_array(a1))