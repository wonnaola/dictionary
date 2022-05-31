n={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
sec=0
third=0
for i in n:
    for j in n:
        if n[i]>max:
            max=n[j]
            a=j
        elif n[j]>sec and n[j]<max:
            sec=n[j]
            b=j
        elif n[j]>third and n[j]<sec:
            third=n[j]
            c=i
print(a,max)
print(b,sec)
print(c,third)
