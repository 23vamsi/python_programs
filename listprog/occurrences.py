
x=[2,4,4,6,4,7,4,4,8]
count=0
y=4
for num in x:
    if(num==y): 
        count=count+1
print("no.of times", y, "occurred is:",count)        


x=[2,4,4,6,4,7,4,4,8]
print(x.count(2))


x=[2,4,4,6,4,7,4,4,8]
count=0
y=input("enter y:")
z=int(y)
for num in x:
    if(num==z): 
        count=count+1
print("no.of times", z, "occurred is:",count)        

