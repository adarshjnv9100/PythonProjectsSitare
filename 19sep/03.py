l = eval(input('Enter the list: '))

n_max = l[0]
for i in l:
    
    if i > n_max:
        n_max = i

print('Maximum number is ', n_max)

