time = int(input("Enter the time: " ))
    
    

mer = input("Enter AM or PM: ")

if mer.upper() == 'AM':
    if time >= 1 and time <= 11:
        print("Good Morning!")
    elif time == 12:
        print("Good Evening!")
    
elif mer.upper() == 'PM':
    if time == 12 or (time >= 1 and time <= 5):
        print("Good AfterNoon!")
    elif time > 5 and time <= 11:
        print("Good Evening!")

else:
    print("Invalid Time!")
