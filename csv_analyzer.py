with open('students.csv','r') as file:
    data = file.readlines()

total_studs = 0
total_marks = 0
mumbai_students = 0


for line in data[1:]:
    student = line.strip().split(',')
    name = student[0]
    marks =int( student[1])
    city = student[2]

    total_studs +=1
    total_marks += marks
    
    if city == 'mumbai':
        mumbai_students+=1
    else:
        pass

avg_marks = total_marks / total_studs

print(f'Total Students {total_studs}')
print(f'Total Marks {total_marks}')
print(f'Average Marks {avg_marks}')
print(f'Mumbai Students {mumbai_students}')