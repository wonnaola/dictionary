a= {'a':50,'b':58,'c': 56,'d':40,'e':100, 'f':20}
d=[]
max=0
sec=0
third=0
for i in a:
    for j in a:
        if a[j]>max:
            max=a[j]
            m=j
        elif a[j]>sec and a[j]<max:
            sec=a[j]
            s=j
        elif a[j]>third and a[j]<sec:
            third=a[j]
            t=j
d.append(m)
d.append(s)
d.append(t)
print(d)

        

