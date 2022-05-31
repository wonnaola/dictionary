p={2:5,3:6,6:7,8:4}
max=0
max_key=None
l={}
for i in p:
    if p[i]>max:
        max=p[i]
        max_key=i
l[max_key]=max
# print(max)
# print(max_key)
print(l)