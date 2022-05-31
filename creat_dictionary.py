i=0
a=[]
while i<15:
    user=int(input("enter the number"))
    a.append(user)
    i+=1
print(a)
j=0
c={}
while j<len(a):
    c[a[j]]=a[j]*a[j]
    j+=1
print(c)

