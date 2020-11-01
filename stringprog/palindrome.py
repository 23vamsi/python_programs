x=input("enter your word:")
y=x[::-1]
if(y==x):
    print("palindrome")
else:
    print("not a palindrome")


x=input("enter your word:")
y=reversed(x)
output="".join(y)
if(output==x):
   print("palindrome")
else:
    print("not a palindrome")