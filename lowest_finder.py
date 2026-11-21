with open('students.csv','r') as file :
    data = file.readlines()

lowest_marks = 100
lowest_student = ''

for line in data[1:]:
    student = line.strip().split(',')
    name= student[0]
    marks = int(student[1])
    city = student[2]

    if marks < lowest_marks:
        lowest_marks = marks
        lowest_student = name

print('Lowest Student:', lowest_student)
print('Lowest Marks',lowest_marks)