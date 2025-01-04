# Ask the user for a string and replace all the vowels with a symbol (e.g., *).
"""Foydalanuvchidan qatorni so'rang va barcha unlilarni belgi bilan almashtiring (masalan, *)."""



txt = input("Enter text: ")
txt = txt.replace('a','*')
txt = txt.replace('e','*')
txt = txt.replace('i','*')
txt = txt.replace('o','*')
txt = txt.replace('u','*')
print(txt)