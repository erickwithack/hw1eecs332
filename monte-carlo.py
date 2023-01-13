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



def sim(num_simulations):
    result = []
    for v in range(1, 100, 10):
        b = getmyBid(v)
        timesWon = 0
        for _ in range(num_simulations):
            otherBid = getOtherBids(v)[random.randint(0, 9)]
            if b > otherBid:
                timesWon += 1          
        result.append(timesWon / num_simulations)
    return result


def getUtility(num_simulations):
    result = []
    for v in range(1, 100, 10):
        b = getmyBid(v)
        utils = []
        for _ in range(num_simulations):
            otherBid = getOtherBids(v)[random.randint(0, 9)]
            if b > otherBid:
                util = float(v) - float(b)
                utils.append(util)                
        result.append(mean(utils))
    return result
 
def getOptimalBid(iters = 100):
    
    optBids = []
    maxUtils = []
    
    for v in range(1, 100, 10):
        b = getmyBid(v)
        
        optBid = float("inf")
        maxUtil = 0
        
        for _ in range(iters):
            otherBid = getOtherBids(v)[random.randint(0, 9)]
            optBid = min(b, otherBid)
            util = float(v) - float(optBid)
            maxUtil = max(maxUtil, util)
        
        optBids.append(util)
        maxUtils.append(maxUtil)
        
    return [optBids, maxUtils]
       

import matplotlib.pyplot as plt
util, bids = getOptimalBid(100)

print(util)
print(bids)

plt.plot(util, 'r', label="utility")
plt.plot(bids, 'b', label="Optimal bids")
plt.ylabel('Optimal Bids and Maximum Utility under Monte Carlo')
plt.legend(loc="upper left")
plt.show()
