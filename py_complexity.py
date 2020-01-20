import numpy as np
import time

'''
  x : takes an input array of intager
  return : a float value of even sum
'''
def evenSummation(x):
    evenSum = 0 # OP1: initializing sum temp variable 
    n = len(x)  # OP2: find array length 
    for i in range(n): # iterating array n times
        if np.mod(x[i],2) == 0: # OP3: check if a number is even?
            evenSum = evenSum + x[i] #OP4: adding eval values
    return evenSum #OP5: returning the values

# Input date size n = 5
n = 500000
# preparing data of size n
x  = np.arange(n)  # assign values to an array

# measering tim,e taken by a python function
t0 = time.time()

evenSum = evenSummation(x) # function calling

t1 = time.time()
total = t1-t0 # total time
print('time taken by python is (sec): ',total)
