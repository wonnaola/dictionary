a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in a:
    for j in a:
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]
        if a[i]<a[j]:
            a[j],a[i]=a[i],a[j]
print(a)