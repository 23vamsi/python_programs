x=[2,4,6,3,1]
i=0
temp=0
while(i<len(x)):
     if(x[i]>temp):
        temp=x[i]
     i=i+1
print("largest number is:",temp) 

x=[2,4,6,3,1]
i=0
temp=999
while(i<len(x)):
     if(x[i]<temp):
        temp=x[i]
     i=i+1
print("smallest number is:",temp) 


x=[2,4,6,3,1]
temp=0
for num in x:
    if(num>temp):
        temp=num
print("maximum number is:",temp)
