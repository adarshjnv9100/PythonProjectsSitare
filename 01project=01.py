def chocopiles(n):
    l = [n]
    for i in range(1,n):
        p = l[-1]
        l.append(p + 2)
    return l

c = int(input("Enter number of chocolate piles: "))

print(chocopiles(c))
