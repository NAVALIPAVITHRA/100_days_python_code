print("welcome to the tip caluclator")
total_bill=float(input("what was the total bill? "))
tip=int(input("how much do u want to give 12 or 15?"))
if tip==12 or tip== 15 :
      tip_total=tip/100
      total_tip_amount=tip_total*total_bill
      final_bill=total_bill+total_tip_amount
      members=int(input("enter the people to spilt the bill "))
      each_bill= final_bill/members
      final_amount= "{:.2f}".format(each_bill)
      print(f"each person should pay: ",final_amount)
else:
   print("give the tip based on the mentioned options")
 