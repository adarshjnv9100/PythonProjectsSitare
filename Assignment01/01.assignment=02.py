n = int( input("Enter a number: "))

if n<0:
    print("Enter a positive number")

elif n == 0 or n == 1:
    print("Factorial of given number is 1")

else:
    f = 1
    for i in range(2, n+1):
        f = f*i
    print("Factorial of given number is ", f)
