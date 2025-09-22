l = eval(input('Enter the list: '))
d = {}

for i in l:
    if i[0] in d:
        d[i[0]].append(i)

    else:
        d[i[0]] = [i]

    
print(d)
