d={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
e={}
for i,j  in d.items():
    c=i.split()
    e["".join(c)]=j
print(e)