height=int(input("enter the height of the person: "))
if height>=120:
    print("u can ridee the rollercoaster")
    age=int(input("enter ur age: "))
    if age<12:
        print("pay $12")
    elif age>18:
        print("pay $13")
    else:
        print("pay $32")
else:
    print("too short for the ride")