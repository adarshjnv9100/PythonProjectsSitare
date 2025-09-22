s = set()
n = input('Enter input: ')
for i in n:
    if i.isnumeric():
        s.add(int(i))

print('Unique numbers :',s)
l = list(s)
count = 0
suml = 0
maxl = l[0]
minl = l[0]

for i in l:
    suml += i
    count += 1
    if i >= maxl:
        maxl = i
    if i <= minl:
        minl = i

print('Count:', count, end=', ')
print('Sum:', suml, end=', ')
print('Avg:', suml/count, end=', ')
print('Max:', maxl, end=', ')
print('Min:', minl)
