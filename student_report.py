cities = {}
with open('students.csv','r') as file:
    data = file.readlines()
 
total_studs = 0
highest_marks = 0
highest_studs = ''
lowest_marks = 100
lowest_studs = ''
passed_studs = 0
failed_studs = 0
for line in data[1:]:
    students = line.strip().split(',')
    name = students[0]
    marks = int(students[1])
    city = students[2]

    total_studs +=1     #to count all students
    if marks >= 40 : # passed 
        passed_studs += 1 
    else :  
        failed_studs +=1
    
    if marks > highest_marks: # finds highest marks 
        highest_marks = marks # stores highest found marks
        highest_studs = name # stores name of highest_studs name 
    
    if lowest_marks > marks: # finds lowest marks 
        lowest_marks = marks # stores lowest found marks
        lowest_studs = name #stores lowest student name 
        
    if city in cities: 
        cities[city] += 1 
    else:
        cities[city] = 1 

print(f'total studs: {total_studs}')
print(f'Passed: {passed_studs}')
print(f'Failed: {failed_studs}')
print('')
print(f'Topper:', highest_studs )
print(f'Highest Marks:', highest_marks)
print('')
print(f'Lowest Student:', lowest_studs)
print(f'Lowest Marks:',lowest_marks)
print('')
print(f'Cities count:',cities)