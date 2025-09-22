n = (int(input("Enter the year: ")))

if n % 400 == 0:
    print('Leap year!')

elif n%100 != 0 and n%4 == 0:
    print('Leap year!')

else:
    print('Not a leap year')
