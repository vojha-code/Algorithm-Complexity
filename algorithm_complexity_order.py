import matplotlib.pyplot as plt
import numpy as np 
import time
# Example of algorithms: https://stackoverflow.com/questions/1592649/examples-of-algorithms-which-has-o1-on-log-n-and-olog-n-complexities


# Algorithm  SUM O(1)
def sumSeries(A):
  n = len(A)
  ans = n*(n+1)/2
  return 1 

# Algorithm  logLoop O(log n)
def logLoop(A):
  count = 0
  for i in range(1,len(A)):
      i /= 2
      count +=1
  return count

# Algorithm  SUM O(n)
def sumArray(A):
  count = 0
  for i in range(len(A)):
    count += 1
  return count


# Algorithm  nLoopsLogLoop O(n log n)
def nLoopsLogLoop(A):
  count = 0
  for i in range(1,len(A)):
    for j in range(len(A)):
      j /= 2
      count +=1
  return count

# Algorithm  Count Distinct Element O(n^2)
def distinctElement(A):
  count = 0
  for i in range(1,len(A)):
    for j in range(len(A)):
      count +=1
  return count


def binary_per(n):
  count = 0
  for i in range(1<<n):
    s = bin(i)[2:]
    s = '0'*(n-len(s))+s
    count += 1
    #print (list(map(int,list(s))))
  return count
    

# input size
nValues = [1,2,4,8]

tValues1 = [] # emplty list for O(1)
tValuesLog = [] # emplty list for O(log n)
tValuesN = [] # emplty list for O(n)
tValuesNlogN = [] # emplty list for O(n log n)
tValuesN2 = [] # emplty list for O(n^2)
tValues2N = [] # emplty list for O(n^2)

for nVal in nValues:
  # input data generation
  a = np.arange(nVal)

  # time computation O(1)
  count = sumSeries(a)
  tValues1.append(count)
  #print('O(1) runtime:',total, b)

  # time computation O(log n)
  count = logLoop(a)
  tValuesLog.append(count)
  #print('O(1) runtime:',total, b)

  # time computation O(n)
  count = sumArray(a)
  tValuesN.append(count)
  #print('O(n) runtime:',total, b)

  # time computation O(n log n)
  count = nLoopsLogLoop(a)
  tValuesNlogN.append(count)
  #print('O(n) runtime:',total, b)
  
  # time computation O(n^2)
  count = distinctElement(a)
  tValuesN2.append(count)

  # time computation O(n^2)
  count = binary_per(len(a))
  tValues2N.append(count)
  #print('O(n^2) runtime:',total, b)


# plotting the points  
print('plotting the graphs:')
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.plot(nValues,tValues1, label='$O(1)$')
ax.plot(nValues,tValuesLog, label='$O(\log_n)$')
ax.plot(nValues,tValuesN, label='$O(n)$')
ax.plot(nValues,tValuesNlogN, label='$O(n \log_n)$')
ax.plot(nValues,tValuesN2, label='$O(n^2)$')
ax.plot(nValues,tValues2N, label='$O(2^n)$')
ax.set_xlabel(' size of n ')
ax.set_ylabel(' running time')
ax.legend()
plt.show()
fig.savefig('graph_order.png')