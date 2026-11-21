with open('student.txt','r') as file:
    data = file.readlines()


for line in data:
    student = line.strip().split(',')
    name = student[0]
    marks = int(student[1])

    if marks >= 40:
        print(name,'PASS')
    else:
        print(name,'FAIL')

