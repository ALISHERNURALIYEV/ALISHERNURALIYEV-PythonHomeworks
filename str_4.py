txt = input("enter text:")
txt = txt.lower()
txt_1 = txt[::-1]
print(txt == txt_1)




#python program to check
#number is palindrome or not
number=int(input("Enter any no:"))
n=number
s=0
while(n):
       r=n%10
       s=s*10+r
       n=n//10
if(s==number):
       print("it is a palindrome")
else:
       print("it is not a palindrome")



