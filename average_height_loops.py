students_height=input().split()
for n in range(0,len(students_height)):
   students_height[n]=int(students_height[n])

total_height=0
for n in students_height:
  total_height+=n
print("total_height :{}".format(total_height))
nof_students=0
for n in students_height:
   nof_students+=1
print(f"number of students:{nof_students}")
  
average_height= total_height/nof_students
print("the average height: {}".format(average_height))
print(round(average_height))

