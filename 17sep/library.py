with open ('C://Users//Administrator//Desktop//Programming methodology in python//project//17sep//library.txt', 'r') as f:
    r = f.read().strip()

    if r:
        d = eval(r)
    else:
        d={}

user = input('Enter the book name: ').lower().strip()

if user in d:
    if d[user] != 0:
        print(user, 'book issued to you.')
        d[user] = d[user] - 1
        print('Library updated.')
    else:
        print('Out of stock.')
else:
    print('Not found.')


with open ('C:/Users/Administrator/Desktop/Programming methodology in python/project/17sep/library.txt', 'w') as f:
    f.write(str(d))

