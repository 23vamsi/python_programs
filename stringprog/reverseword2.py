x="hello world"
y=x.split()
z=[]
for i in y:
    z.append(i[::-1])
print(z)