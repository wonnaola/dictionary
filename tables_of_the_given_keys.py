user=int(input("enter the number :"))
i=1
d={}
while i<=user:
    j=1
    a=[]
    while j<=10:
        a.append(i*j)
        d[i]=a
        j+=1
    i+=1
print(d,end="")


# i=1
# while i<=50:
#     print(i,end=" ")
#     print(i+50)
#     i=i+1



    
