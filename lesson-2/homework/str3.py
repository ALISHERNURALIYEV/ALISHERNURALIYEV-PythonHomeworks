#Write a Python program to: Take a string input from the user. Print the length of the string.Convert the string to uppercase and lowercase.  
# foydalanuvchidan matn kiritish uchun python dasturini yozing matn uzunligini chop eting  , matnni katta va kichik harflarga aylantiring

      #012345678901234.....
txt = 'write a Python    program'
print(len(txt))        # matn uzunligi
print(txt.lower())       # barcha harflarini kichik harflarga o'tkazish 
print(txt.upper())        # barcha harflarini katta harflarga o'tkazish
print(txt.capitalize())    # faqat so'zni birinchi harfini bosh harfga o'tkazadi 
print(txt.title())       # ichidagi har bir so'zni bosh harfga o'tkazadi
print (txt.lower())     
print(txt.endswith('m'))   # oxiri m bilan tugaydimi?
print(txt.startswith('a'))

print('-'*50)
print(txt.strip())
print (txt.split())      #har bir elementni alohida ko'rsatish


