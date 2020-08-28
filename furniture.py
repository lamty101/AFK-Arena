# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:34:44 2020

@author: 85290
"""
def experiment (expcount):
    
    import random
    result = []
    
    for count in range(expcount):
        a = 0
        b = 0
        c = 0
        while a < 3 or b < 3 or c < 3:
            r = random.randrange(3)
            if r == 0:
                a += 1
            elif r == 1:
                b+=1
            else:
                c+=1
        result.append(a+b+c)
        
    return result

import numpy as np

result = experiment(1000000)
(unique, counts) = np.unique(result, return_counts=True)
frequencies = np.asarray((unique, counts)).T
np.savetxt('result.csv', frequencies, delimiter=',')

print(np.std(result))
print(np.average(result))

