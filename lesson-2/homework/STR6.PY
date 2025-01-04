#Write a Python program to check if one string contains another.
# bir satrda boshqasi borligini tekshirish uchun python programmasini tuzing


txt = input("Enter text :")           # txt ni kiritish
word = input("Word to check :")       # tekshirish so'zi
if word in txt.split():               # agar tekshirish so'zi txt da bo'lsa 
       print("Yes")
else:                                  # aks holda 
    print("No")