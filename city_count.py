cities = {}
with open('students.csv','r') as file:
    data = file.readlines()
for line in data[1:]:
    student = line.strip().split(',')

    city = student[2]
    # print(city)
    if city in cities :
        cities[city] += 1
    else:
        cities[city] = 1

print(cities)