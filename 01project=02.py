def check_list(li):
   
    if len(set(li)) != 5:
        return False
    for i in range(1, len(li)):
        if li[i] == li[i-1]:
            return False
    
    return True

x = [1,2,3,4,5,1,2,3,4,5]
y = [1,2,2,3,4,5,5,1,2,3,4]
z = [1,5,6,7,2,1,6,2,7,5]
print(check_list(x))
print(check_list(y))
print(check_list(z))
