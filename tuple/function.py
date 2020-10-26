
def add(x,y=5):
    count=x+y
    return count

def sub(c,d):
    count=c-d
    return count

def arrfunc(arrtemp):
    i=0
    j=0
    #while(i<len(arrtemp)):
        #j=j+arrtemp[i]
        #i=i+1
    for x in arrtemp:
        j=j+x
    return j
        
#arr=[2,3,5,6]
#j=2
#i=1
#j=4


a=24
b=23
addoutput=add(a,b)
print(addoutput)


suboutput=sub(a,b)
print(suboutput)

addsingle=add(a)
print(addsingle)

arr=[2,4,5,6]
arrsum=arrfunc(arr)
print(arrsum)


