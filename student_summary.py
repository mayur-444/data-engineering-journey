with open('student.txt','r') as file:
    data = file.readlines()

passed_students = 0
failed_students = 0
total_students = 0
for line in data :
    student = line.strip().split(',')
    try:
        marks=int(student[1])
        total_students+=1

        if marks >= 40:
            passed_students += 1
        else :
            failed_students += 1
    except ValueError:
        print('Invalid Record Found:', line.strip())
print('Total Students', total_students)
print('Passed Students:',passed_students)
print('Failed Students:',failed_students)
    