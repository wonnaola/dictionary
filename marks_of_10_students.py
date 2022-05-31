i=0
a=[]
b=[]
while i<10:
    user1=input("enter the name :")
    user2=int(input("enter the marks :"))
    a.append(user1)
    b.append(user2)
    i+=1
print(a)
print(b)
j=0
d={}
while j <len(a):
    d[a[j]]=b[j]
    j+=1
print(d)

 
