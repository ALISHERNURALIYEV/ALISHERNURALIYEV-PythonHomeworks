a=int("147")
b=int (159)
c=int("132")
print(min(a, b, c))
print(max(a, b, c))


import heapq
grades = [110, 25, 38, 49, 20, 95, 33, 87, 90]
print(min(grades), max(grades))
print(heapq.nlargest(3,grades))
print(heapq.nsmallest(4, grades))