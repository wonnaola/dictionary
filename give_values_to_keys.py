s=['a','b','c','d']
t=[1,2,3,4]
p={}
i=0
while i<len(s):
    p[s[i]]=t[i]
    i=i+1
print(p)


# a={'a':90,'b':80,'c':70,'d':60}
# b={'e':50}
# c=dict(a,**b)
# print(c)