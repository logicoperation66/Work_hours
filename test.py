from datetime import datetime
from domyslny_arkusz import days_cur_month

for value in days_cur_month():
    year = value[:4]
    month = value[5:7]
    day = value[8:10]
    d = datetime(int(year), int(month), int(day))
    if d.weekday() > 4:
        print(value, 'weekend')
    else:
        print(value, 'weekday')
