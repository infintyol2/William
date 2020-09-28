list= [1]
for i in range(6): 
    print(list) 
    newlist=[] 
    newlist.append(list[0]) 
    for i in range(len(list)-1): 
        newlist.append(list[i]+list[i+1]) 
    newlist.append(list[-1]) 
    list=newlist 
n=5
for a in range(0,n):
    for a1 in range(a):
        print("*", end="")
    print()
for a in range(n,0,-1):
    for a1 in range(a):
        print("*", end="")
    print()