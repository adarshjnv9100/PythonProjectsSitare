import csv

subject_toppers = {}

with open("marks.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        subject = row["subject"]
        name = row["name"]
        marks = int(row["marks"])

        if subject not in subject_toppers:
            subject_toppers[subject] = (marks, [name])
            
        else:
            max_marks, students = subject_toppers[subject]
            if marks > max_marks:
                subject_toppers[subject] = (marks, [name])

            elif marks == max_marks:    
                students.append(name)
                subject_toppers[subject] = (max_marks, students)


for subject, (marks, students) in subject_toppers.items():
    print("Subject:", subject, "→", end=" ")
    for i in range(len(students)):
        if i == len(students) - 1:
            print(students[i], "(", marks, ")", sep="")
        else:
            print(students[i] + ",", end=" ")
