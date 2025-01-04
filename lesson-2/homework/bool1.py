#Write a program that accepts a username and password and checks if both are not empty
""" Foydalanuvchi nomi va parolni qabul qiladigan va ikkalasi ham boʻsh emasligini tekshiradigan dastur yozing"""

username = input("Enter username: ")
password = input("Enter password: ")

print(bool(username) * bool(password) ==1 )