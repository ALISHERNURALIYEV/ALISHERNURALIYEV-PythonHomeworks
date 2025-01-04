"""Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.
Example:
# foydalanuvchidan jumla va uni  almashtirish uchun so'z kiritishni so'rang va uni foydalanuvchi tomonidan taqdim etilgan boshqa so'z bilan almashtiring

# Input sentence: "I love apples."
Replace: "apples"
With: "oranges"
Output: "I love oranges."""

sentence = input("Enter sentence:")
replese = input("Enter replese:")
replese = sentence.replace('sentence', replese)
print(replese)



