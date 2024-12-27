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



#1 Count Occurrences: Given a list and an element, find how many times the element appears in the list.
#1 ro'yxat berilgan bo'lsa element ro'yxatda necha marta ishtirok etganini toping.
#METHOD 1 .
list = [1,13,12,12,12,13,14,15,1,6,12]
x=12
print(list.count(x))

#3  method 3
list = ['a', 'b', 'c' , 'd', 'b', 'b']
x='b' 
print(list.count(x))