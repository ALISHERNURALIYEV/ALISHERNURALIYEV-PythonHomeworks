# Ask the user for a sentence and create an acronym from the first letters of each word.
""" Foydalanuvchidan jumla so'rang va har bir so'zning birinchi harflaridan qisqartma yarating.
Example:

#Input: "World Health Organization"
#Output: "WHO" """


txt = input("Enter text :")
txt = txt.upper()
words = txt.split()

acronym = ''.join(word[0] for word in words)
print(acronym)