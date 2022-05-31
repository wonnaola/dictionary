#Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
#Expected output:
#{'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
i=0
d={}
while i<len(employees):
    d[employees[i]]=defaults
    i+=1
print(d)
