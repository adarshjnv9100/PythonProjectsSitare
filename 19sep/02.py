l = eval(input('enter a list: '))
d = {}

for i in l:
    if i in d:
        d[i] += 1
    
    else:
        d[i] = 1
     

for k,v in d.items():
    print(k,'------>',v)
