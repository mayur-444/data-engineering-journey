file = open('student.txt','r')
data = file.readlines()

total_marks = 0
student_count = 0

highest_mark = 0
topper = ''

for line in data:
    student = line.strip().split(',')

    name =student[0]
    marks = int(student[1])

    total_marks += marks
    student_count += 1

    if marks > highest_mark:
        highest_mark = marks
        topper = name

average_marks = total_marks / student_count

print('Total Students:',student_count)
print('Total Marks:',total_marks)
print('Average Marks:',average_marks)
print('Topper:',topper)
print('Highest Marks:',highest_mark)

file.close()