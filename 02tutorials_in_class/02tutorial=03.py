l = eval(input("Enter the list: "))
thres = int(input("Enter the threshhold value: "))

def find_indexes(li,thr):
    indexlist = []
    for i in range(len(li)):
        if li[i] < thr:
            indexlist.append(i)

    return indexlist

print(find_indexes(l, thres))
