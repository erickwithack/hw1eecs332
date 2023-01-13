import csv
import random
from statistics import mean

def readRow(number):
  result = []
  with open('Data.csv', 'r') as f:
      csv_reader = csv.reader(f, delimiter=',')
      iter = 0
      for row in csv_reader:
          if iter == number:
            result.append(row)
            break
          iter += 1
  return result[0]


def getmyBid(value):
  return readRow(1)[(int(value/10)) - 1]

def getOtherBids(value):
  n = int(value / 10) - 1
  file_name = "Data.csv" 
  f = open(file_name)
  csv_file = csv.reader(f)
  second_column = [] 
  for line in csv_file:
      second_column.append(line[n])
  return second_column[2:]


def timesWon(value):
  b = getmyBid(value)
  others = getOtherBids(value)
  timesWon = 0
  for bid in others:
    if b > bid:
      timesWon += 1
  return timesWon/len(others)


def getTotalProb():
  result = []
  for v in range(1, 100, 10):
    prob = timesWon(v)
    result.append(prob)
  return result


def getTotalUtility():
  result = []
  for v in range(1, 100, 10):
    b = getmyBid(v)
    others = getOtherBids(v)
    
    utils = []
    
    for opp in others:
      if b > opp:
        util = float(v) - float(b)
        utils.append(util)
        
    result.append(util)  
  return result
        


def getOptimalBid():
  opBids = []
  utils = []
  
  optimalBid = float("inf")
  maxUtil = 0
  
  for v in range(1, 100, 10):
    b = getmyBid(v)
    others = getOtherBids(v)
    
    lowestBid = min(others)
    l = float(min(b, lowestBid))
    
    optimalBid = min(optimalBid, l) 
    u = float(v) - float(optimalBid)
    
    maxUtil = max(maxUtil, u)
    
    utils.append(maxUtil)
    opBids.append(optimalBid) 
    
  return [utils, opBids]



import matplotlib.pyplot as plt
util, bids = getOptimalBid()

print(util)
print(bids)

plt.plot(util, 'r', label="utility")
plt.plot(bids, 'b', label="Optimal bids")
plt.ylabel('Optimal Bids and Maximum Utility under Exact Calculations')
plt.legend(loc="upper left")
plt.show()



        
