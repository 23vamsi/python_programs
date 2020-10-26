#WRITE A PROGRAM to check count of elements in the list even or not

x=[1,2,3,2,4,5]
count=0
for num in x:
    if(num%2==0):
        count=count+1
print("total no.of even numbers are:", count)


x=[2,4,6,3,1]
i=0
temp=99999
while(i<len(x)):
     if(x[i]<temp):
        temp=x[i]
     i=i+1
print("maximum number is:",temp)        

table=7
i=1
j=1
while(i<=table):
    while(j<=10):
        print(i,"x",j,"=",i*j)
        j=j+1   
    i=i+1
    j=1
    
        



