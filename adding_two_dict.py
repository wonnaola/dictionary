d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 2009, 'd':400}
for i in d1:
    for j in d2:
        if i==j:
            d1[i]=d1[i]+d2[j]
d2.update(d1)
print(d2)