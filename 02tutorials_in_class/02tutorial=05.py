def element_length(li):
    n = []
    for i in li:
        n.append(len(i))
    return n

l = eval(input("Enter the list: "))
if l != []:
    print(element_length(l))

else:
    print("List is empty.")
