import pandas as pd

student_dict = {
    "Name": ["abi", "sabu"],
    "Age": [24, 23]
}
print(student_dict)
student_frame = pd.DataFrame(student_dict)
print(student_frame)
for key,value in student_dict.items():
    print(f"key :{key} and value :{value}")
for key,value in student_frame.iterrows():
     print(f"key :{key} and value :{value}")
for key,value in student_frame.items():
     print(f"key :{key} and value :{value}")