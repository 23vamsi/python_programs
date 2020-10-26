x=[1,2,3,1,4,1,3,1,2,1,1]
d={1:4,5:0,3:1}
for k in x:
    if(k in d):
        d[k]=d[k]+1
    else:
        d[k]=1    
#print(d.keys())
for y in d.keys():
    print(y,d[y])


#d[1] 10
#d[2] 2
#d[3] 3
#d[4] 1

