# x= {'list1': [4, 7, 10, 20], 'list2': [7, 16, 9, 10], 'list3': [13, 10, 4, 8], 'list4': [7, 20, 6, 11]}
# #Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]
# a=[]
# for i in x:
#     if x[i] not in a:
#         a.append(x[i])
#     j=0
#     b=[]
#     while j<len(a):
#         k=0
#         while k<len(a[j]):
#             if a[j][k] not in b:
#                 b.append(a[j][k])
#                 b.sort()
#             k+=1
#         j+=1
# print(b)



# a=[]
# for i in x:
#     a.extend(x[i])
# j=0
# b=[]
# while j<len(a):
#     if a[j] not in b:
#         b.append(a[j])
#     j+=1
# b.sort()
# print(b)      



# a="my name is themsingla"
# b=a.split()
# d={}
# i=0
# while i<len(b)-1:
#     i+=1
# c=b[i]
# d[b[i]]=1
# print(d)
