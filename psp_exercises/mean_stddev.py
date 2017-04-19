import math

def mean(data):
  sum = 0
  for i in range(len(data)):
    el = data[i]
    sum += el
  return sum/len(data)

def stddev(data, mean):
  sum = 0
  for i in range(len(data)):
    el = data[i]
    squared_error = math.pow(el-mean, 2)
    sum += squared_error 
  return math.sqrt(sum/(len(data)-1))

def mean_stddev(data):
  x_bar = mean(data)
  sx = stddev(data, x_bar)
  return x_bar, sx
