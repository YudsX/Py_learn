import datetime

date = datetime.datetime.now()
# return this all output to a integer / Numbers
print(f"Date time Now: {date}")
print(f"Date time Year Now: {date.year}")
print(f"Date time Month Now: {date.month}")
print(f"Date time Hour Now: {date.hour}")
print(f"Date time Day Now: {date.day}")

# By strftime 
print(f"Day Time by strf: {date.strftime("%A")}")