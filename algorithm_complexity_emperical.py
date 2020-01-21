import matplotlib.pyplot as plt
import numpy as np 
import time
# Example of algorithms: https://stackoverflow.com/questions/1592649/examples-of-algorithms-which-has-o1-on-log-n-and-olog-n-complexities


# Algorithm  SUM O(1)
def sumSeries(A):
  n = len(A)
  return n*(n+1)/2

# Algorithm  logLoop O(log n)
def logLoop(A):
  count = 0
  i = len(A)
  while i > 1:
      i /= 2
      count +=1
  return count

# Algorithm  SUM O(n)
def sumArray(A):
  sum = 0
  for i in range(len(A)):
    sum = sum + A[i]
  return sum


# Algorithm  nLoopsLogLoop O(n log n)
def nLoopsLogLoop(A):
  count = 0
  n = len(A)
  for i in range(n):
    j = n
    print(i, end='  ')
    while j > 1:
        j /= 2
        count +=1
  return count

# Algorithm  Count Distinct Element O(n^2)
def looN2(A):
  count = 0
  for i in range(1,len(A)):
    for j in range(len(A)):
      count +=1
  return count

# input size
#nValues = [1,5,10,50,100,500,1000]
nValues = [1,5,10,50,100,200,500]

tValues1 = [] # emplty list for O(1)
tValuesLog = [] # emplty list for O(log n)
tValuesN = [] # emplty list for O(n)
tValuesNlogN = [] # emplty list for O(n log n)
tValuesN2 = [] # emplty list for O(n^2)

for nVal in nValues:
  # input data generation
  a = np.arange(nVal)

  # time computation O(1)
  t0 = time.time()
  b = sumSeries(a)
  t1 = time.time()
  total = t1-t0
  tValues1.append(total)
  #print('O(1) runtime:',total, b)

  # time computation O(log n)
  t0 = time.time()
  b = logLoop(a)
  t1 = time.time()
  total = t1-t0
  tValuesLog.append(total)
  #print('O(1) runtime:',total, b)

  # time computation O(n)
  t0 = time.time()
  b = sumArray(a)
  t1 = time.time()
  total = t1-t0
  tValuesN.append(total)
  #print('O(n) runtime:',total, b)

  # time computation O(n log n)
  t0 = time.time()
  b = nLoopsLogLoop(a)
  t1 = time.time()
  total = t1-t0
  tValuesNlogN.append(total)
  #print('O(n) runtime:',total, b)

  # time computation O(n^2)
  t0 = time.time()
  b = looN2(a)
  t1 = time.time()
  total = t1-t0
  tValuesN2.append(total)
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
ax.set_xlabel(' size of n ')
ax.set_ylabel(' running time')
ax.legend()
plt.show()
fig.savefig('graph_emperical.png')
