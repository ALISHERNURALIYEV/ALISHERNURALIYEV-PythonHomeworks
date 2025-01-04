# Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
""" Raqamni qabul qiladigan va uning 3 va 5 ga bo'linishini tekshiradigan dastur yarating."""

num = int(input("Enter number: "))
print(num%3==0 and num%5==0)