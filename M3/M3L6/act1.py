print("Hi! We are going to check the exact date and time .")

from datetime import date ,time, datetime

today = date.today()
now = datetime.now

print("Today, the date is ",today,".")
print("\nThe current date and time is ",now,".")

print("\nData componenets are ",today.year , today.month , today.day,".")