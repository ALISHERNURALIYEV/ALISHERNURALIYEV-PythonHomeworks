#Create a program that converts kilometers to meters and centimeters.
# km ni m va sm ga aylantiradigan dastur yarating.

km = int(input("Enter kilometers:"))
m = km*1000
sm = km*1000*100

print("{} meters".format(m) )
print("{} centimeters".format(sm))