#=========================== P4 ============================#


#====== Part 1 =========#

import numpy as np
import pandas as pd

passwords = pd.read_csv('inputs/Problem2.csv')
passwords = passwords.iloc[:, 0].str.split(expand = True)
df = pd.DataFrame(columns = ['lowest', 'highest', 'letter', 'password'])
df['lowest'] = passwords[0].str.split('-').str[0]
df['highest'] = passwords[0].str.split('-').str[1]
df['letter'] = passwords[1].str.split('').str[1]
df['password'] = passwords[2]
df.head()



def number_of_times(a,b):
    x = 0
    for i in range(len(b)):
        if(b[i] == a):
            x = x + 1
        else:
            continue
    return x


valid_passwords = 0
for i in range(df.shape[0]):
    row = df.iloc[i,:]
    a = row['letter']
    b = list(row['password'])
    if(int(row['lowest']) <= int(number_of_times(a,b)) <= int(row['highest'])):
        valid_passwords = valid_passwords + 1
    else:
        continue

print('Number of valid passwords', valid_passwords)



#==================== Part 2=================#
def check_password(pos1, pos2, letter, password):
    n = 0
    if(password[pos1 -1] == letter):
        n = n +1
    if(password[pos2 -1] == letter):
        n = n + 1
    else:
        n = n + 0
    return n


valid_passwords = 0
for i in range(df.shape[0]):
    row = df.iloc[i,:]
    pos1 = int(row['lowest'])
    pos2 = int(row['highest'])
    letter = row['letter']
    password = row['password']
    if(int(check_password(pos1, pos2, letter, password)) == 1):
        valid_passwords = valid_passwords + 1
    else:
        continue

print('Number of valid passwords', valid_passwords)











