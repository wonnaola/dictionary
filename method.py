# # update meth0ds:
# a={1:2,2:3,3:4}
# a1={1:0}
# a.update(a1)
# print(a)

# # values method():

# a={1:2,2:3,3:4}
# d=a.values()
# print(d)

# # key method():
# a={1:2,2:3,3:4}
# d=a.keys()
# print(d)

# # items():

# a={1:2,2:3,3:4}
# b=a.items()
# print(b)

# # get() method..
# a={1:2,2:3,3:4}
# b=a.get(3)
# print(b)

# # pop():
# a={1:2,2:3,3:4}
# a.pop(3)
# print(a)

# # popitem():
# a={1:2,2:3,3:4,7:9}
# a.popitem()
# print(a)


# # clear()
# a={1:2,2:3,3:4,7:9}
# a.clear()
# print(a)

# # setdefault()
# a={1:2,2:3,3:4,7:8}
# print(a.setdefault("ID","no ID"))
# # print(a.setdefault(7))
# print(a)

# # fromkey()
# a={1,2,3}
# b=dict.fromkeys(a,"themsingla")
# print(b)