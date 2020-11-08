def make_schedule(period1, period2,period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title()+", [3rd] "+ period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history","science")
print("SCHEDULE:", student_schedule)