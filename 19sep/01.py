l = eval(input('Enter the list: '))
nl = []
for i in l:
    if i not in nl:
        nl.append(i)

print(nl)
