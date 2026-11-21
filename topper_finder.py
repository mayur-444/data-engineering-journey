with open('students.csv','r') as file:
    data = file.readlines()

highest_marks = 0
topper = ''

for line in data[1:]:
    student = line.strip().split(',')
    name = student[0]
    marks = int(student[1])

    if marks > highest_marks:
        highest_marks = marks 
        topper = name
    

print('topper:', topper)
print('highest marks :', highest_marks)
