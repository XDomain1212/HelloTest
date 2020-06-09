from datetime import datetime,timedelta
today=datetime.now()
today_date=today.strftime("%Y-%m-%d")
print("Today is : " + str(today_date))

# oneday=timedelta(weeks=1)
# yesterday=today-oneday
# print("Yesterday is "+ str(yesterday))
# birthday=input("Please input your Birthday(dd/mm/yyyy): ")
# birthday_date=datetime.strptime(birthday,"%d/%m/%Y")
# print('Your birthday is :' + str(birthday_date))