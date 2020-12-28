import math
import numpy as np
import pandas as pd

df = pd.read_csv('inputs/problem3.csv', header = None)
df = df.iloc[:, 0].str.split('',expand = True)
df = df.iloc[:,1:df.shape[1] - 1]
df = df.replace('.',0)
df = df.replace('#',1)
df = df.to_numpy()
dfshape


def map_stacking(right_steps):
    matrix = np.copy(df)
    x = np.copy(matrix)
    y = int(math.ceil(matrix.shape[0]*right_steps)/matrix.shape[1])
    for i in range(y):
     matrix = np.hstack((matrix,x))
    return matrix


def tree_counting(right_steps, down_steps):
    row = 0
    col = 0
    tree = 0
    tree_map = map_stacking(right_steps)
    for i in range(math.ceil(tree_map.shape[0]/down_steps)):
        if(tree_map[row, col] == 1):
         tree = tree + 1
        else:
         tree = tree + 0
        col = col + right_steps
        row = row + down_steps
    return tree



#=========== Part 1 ============#

print('Number of trees along the slope :',tree_counting(3,1))


#=========== Part2 ============#
right = np.array([1,3,5,7,1])
down  = np.array([1,1,1,1,2])
prod = 1
for i in range(right.size):
     tree = tree_counting(right[i], down[i])
     print(tree)
     prod = prod * tree

print('The product is :', prod)


















