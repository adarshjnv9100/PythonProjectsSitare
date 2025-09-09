s = input("Enter the news: ")

a = e = i = o = u = 0
for x in s:
    if i == "a":
        a += 1

    elif i == "e":
        e += 1

    elif i == "i":
        i += 1

    elif i == "o":
        o += 1

    elif i == "u":
        u += 1

w = s.split()
wdic = {}

for word in w:
    if word in wdic:
        wdic[word] += 1
    else:
        wdic[word] = 1

print('a: ', a, 'i: ', i, 'o: ', o, 'u: ', u, 'e: ', e )
for i in wdic:
    print(i, ':', wdic[i], end=', ')   
