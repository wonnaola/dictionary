dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic1:
    if i in dic2:
        dic2[i]=dic1[i]+dic2[i]
dic1.update(dic2)
dic1.update(dic3)
print(dic1)