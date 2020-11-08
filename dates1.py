from datetime import datetime,timedelta
today = datetime.now()
print("Today: "+str (today))
one_day = timedelta(days = 1)
tom = today+one_day
print("Tomorrow: "+str(tom))
one_week = timedelta(weeks = 1)
next_week = today + one_week
print("Next Week: "+ str(next_week))
