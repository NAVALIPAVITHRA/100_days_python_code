name1=input()#pavithra navali
name2=input()#kavya navali
combined_names=name1+name2
print(combined_names)#pavithra navalikavya navali
lower_names=combined_names.lower()
t=lower_names.count("t")#1
r=lower_names.count("r")#1
u=lower_names.count("u")#0
e=lower_names.count("e")#0
first_digit=t+r+u+e#2
l=lower_names.count("l")#2
o=lower_names.count("o")#0
v=lower_names.count("v")#4
e=lower_names.count("e")#0
second_digit=l+o+v+e#6
score=int(str(first_digit)+str(second_digit))#26

if(score<10 ) or (score >90):
    print(f" your score is {score}.")
elif (score>=40)and (score<=50):
    print(f"ur score is {score}")
else:
    print(score)#26