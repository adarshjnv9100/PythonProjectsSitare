'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == 0 or num2 == 0:
    print("YOU HAVE ENTERED ZERO!")

while num2 != 0:
    num1 = num2
    num2 = num1 % num2

print('GCD of given numbers is ', num1)

'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == 0 or num2 == 0:
    print('You have entered zero!')
else:
    
    n = min(num1, num2)

    for i  in range(n, 0, -1):
        if (num1 % i == 0) and (num2 % i ==0):
            print("GCD of given number is ", i)
            break
