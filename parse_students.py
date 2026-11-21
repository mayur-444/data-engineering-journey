file = open('student.txt','r')

data = file.readlines()

for line in data:
    student = line.strip().split(',')

    name = student[0]
    marks = int(student[1])
    print('Name:',name)
    print('Marks:',marks)
    print('-----')

file.close()