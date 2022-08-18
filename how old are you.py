
dob=int(input('enter the date of birth:'))

print(dob)
from datetime import date

today = date.today()
print(today.year)
print("Today's date:", today)


print("now you are",today.year-dob,"years old")
