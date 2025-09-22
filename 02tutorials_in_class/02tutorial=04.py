
def check_palindrome(li):
    res = []
    for i in li:
        i = i.lower()
        if i == i[::-1]:
            res.append(True)
        else:
            res.append(False)

    return res

l = eval(input("Enter the list of stings: "))
print(check_palindrome(l))
