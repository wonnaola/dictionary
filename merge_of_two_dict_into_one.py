a= {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
b= {'Thirty': 30, 'Fourty': 40, 'Fifty':50}
for i in a:
    if i in b:
        continue
a.update(b)
print(a)