def printarray(arr,arr1,arr2,arr3):
    print(arr,arr1,arr2,arr3.keys())

def variablearg(*var):
    print("length of arguments are:",len(var))
    print(var[0])




x=[1,4,"arr",6,"func"]
y=[2,1,"sum",3,"add"]
z=10
v={1:"hii",2:"bye"}
printarray(x,y,z,v)

print(type(x))

print(type(y))


print(type(z))

print(type(v))


variablearg(x,y)


