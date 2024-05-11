#!/usr/bin/env python3

import os

os.system('ls -l')
# check system time
os.system('date')

##- get list of files in dir
file_list = os.listdir()
print(file_list)
assert 'LICENSE' in file_list

print(file_list)

#- get the bitcoin price
assert bitcoin_value > 60000

print("bitcoin_value:", bitcoin_value)
