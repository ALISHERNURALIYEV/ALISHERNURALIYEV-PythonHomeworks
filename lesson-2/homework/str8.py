#Write a program that asks the user for a string and prints the first and last characters of the string.
""" Foydalanuvchidan satr so‘raydigan va satrning birinchi va oxirgi belgilarini chop etadigan dastur tuzing."""


word = input("Enter a word:")
first_letter = word.split()[0]
last = word.split()[-1]
print(last)