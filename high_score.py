student_score=input().split()
for n in range(0,len(student_score)):
     student_score[n]=int(student_score[n])

'''student_score.sort()
print(student_score)

print(student_score[-1])'''
high=0
for score in student_score:
     if score>high:
          high=score
          
print(high)