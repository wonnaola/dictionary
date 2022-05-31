# Print the value of key ‘history’ from the below dict
# a= {"class": {"student": {"name": "Mike","marks": {"physics": 70,"history": 80}}}}
# print(a["class"]["student"]["marks"]["history"])

a=["432"]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        c=int(a[i][j])* int (a[i][j])
        print(c)
        j+=1
    i+=1
 