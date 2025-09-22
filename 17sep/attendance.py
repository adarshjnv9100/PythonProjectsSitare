master = [1,2,3,4,5,6,7,8,9,10]

with open('attendance.txt','r') as f:
    present = []
    for line in f:
        present.append(int(line.strip()))
    print("Present roll number:", present)


absent = [roll_no for roll_no in master if roll_no not in present]
print("Absent roll number:", absent)

with open('absent.txt','w') as f:
    for roll_no in absent:
        f.write(str(roll_no))
        f.write('\n')


print('Absent.txt created succesfully')
