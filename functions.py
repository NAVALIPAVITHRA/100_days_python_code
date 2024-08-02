def is_year(year):
    if year%4==0:
        if year%100==0:
            if year%400 ==0:
               return True
            else:
              return False
        else:
           return True
    else:
           return False
def days(year,month):
    months=[31,28,31,30,31,30,31,31,30,31,30,31]
    if month==2 and is_year(year):
        return 29
    else:
        return months[month-1]
year=int(input())
month=int(input())
days=days(year,month)
print(days)