a={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
#{'red': 3, 'green': 5, 'black': 5, 'white': 5}
d={}
for i in a:
    c=len(a[i])
    d[a[i]]=c
print(d)
