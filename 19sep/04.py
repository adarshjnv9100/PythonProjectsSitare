with open('C://Users//Administrator//Desktop/Programming methodology in python//project//19sep//error.txt') as f:
    for line in f:
        if 'error' in line.lower():
            print(line.strip())
