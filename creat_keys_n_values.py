# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
a='w3resource'
d={}
count=0
for i in a:
    if i in d:
        d[i]+=1
    else:
       d[i]=1
print(d)
