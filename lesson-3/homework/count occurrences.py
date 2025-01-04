#1 METHOD  2
from collections import Counter


list = [1, 13, 12, 12, 12, 13, 14, 15, 1, 6, 12]
count=dict()
  
for i in list:
      if i in count:
        count[i]+=1
      else:
          count[i]=1
print(count)



