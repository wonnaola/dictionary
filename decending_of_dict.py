a={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
for i in a:
    for j in a:
        if a[j]>a[i]:
            a[i],a[j]=a[j],a[i]
        if a[i]>a[j]:
            a[j],a[i]=a[i],a[j]
print(a)
