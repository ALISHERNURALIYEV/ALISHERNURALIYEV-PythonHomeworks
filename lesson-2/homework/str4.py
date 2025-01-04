#Write a Python program to check if a given string is palindrome or not.
#What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one.
# Example: “madam”, “racecar”, “12321”

""" berilgan satr palindrom yoki yo'qligini tekshirish uchun python dasturini tuzing .  palindrom qatori nima ? -- Agar satrning teskarisi
uni asli bilan bir xil bo'lsa u holda u satrni palindrom deymiz"""


word = input ("Enter a string:")
opposite = word[::-1]
print(word==opposite)

