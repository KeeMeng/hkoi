num_schools = int(input())
schools = []
for i in range(num_schools):
    school = input().split("  ")
    schools.append([int(school[0]), int(school[1]), 0, 0])
    
num_students = int(input())
students = []
for i in range(num_students):
    student = []
    temp = input().split("  ")
    for s in temp[:-1]:
        student.append(int(s))
    student.append(float(temp[-1]))
    students.append(student[1:])

#print(schools)
# id  avaliable  filled  sum

#print(students)
# 1st  2nd  3rd  score

count1 = 0
while count1 < num_students:
    #each student
    
    count2 = 0
    while count2 < num_schools:
        #student's school
        count3 = 0
        check = False
        while count3 < num_schools:
            #schools
            if schools[count3][0] == students[count1][count2] and schools[count3][2] < schools[count3][1]:
                schools[count3][2] += 1
                schools[count3][3] += students[count1][3]
                #print(schools[count3][0])
                check = True
                break
            count3 += 1
        if check:
            break
        count2 += 1
    count1 += 1

count = 0
while count < num_schools:
    if schools[count][3] != 0:
        schools[count][3] = schools[count][3] / schools[count][2]
    count += 1

#print(schools)
#print(students)

print("School    No. of students    Average score")
print("******************************************")
for school in schools:
    if school[2] != 0
    print(f"  {str(school[0])}             {str(school[2])}               {str(round(school[3], 2))}    ")
