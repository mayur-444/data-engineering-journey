# import os
# print(os.getcwd())

with open('raw_students.csv','r') as file:
    data = file.readlines()

clean_records = []

clean_records.append('name,marks,city\n')

for line in data[1:]:
    student = line.strip().split(',')

    name = student[0].strip()
    marks = student[1].strip()
    city = student[2].strip()
    try:
        marks = int(marks)

        clean_record = f'{name},{marks},{city}\n'

        clean_records.append(clean_record)
    except ValueError:
        print('Invalid Record Removed', line.strip())

with open('clean_students.csv','w') as file:
    file.writelines(clean_records)

print('Clean File created successfully!')