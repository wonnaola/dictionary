# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# dic1={}
# for i in dic:
#     if dic[i]not in dic1:
#         dic1[i]=dic[i]
# print(dic1)


dict={"key1":10,"key2":20,"key3":30,"key4":40,"key5":50}
a=[]
# c=0
# for i in dict:
#     c+=dict[i]
# a.append(c)
# print(a)

for i in dict:
    if i in dict:
        b=[]
        b.append(i)
        b.append(dict[i])
    a.append(b)
print(a)

