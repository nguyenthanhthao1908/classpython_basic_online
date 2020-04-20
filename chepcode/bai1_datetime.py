
from datetime import datetime       #class datetime from module datetime
import pytz                         #truy cap thu vien pytz

local = datetime.now()              #tra ve ngay-gio hien tai
print("local:", local.strftime("%m/%d/%Y, %H:%M:%S"))       #in ra man hinh ngay-gio

tz_NY = pytz.timezone('America/New_York')       #chuyen doi mui gio, Time zone argument is New_York
datetime_NY = datetime.now(tz_NY)           #tra ve ngay-gio hien tai cua New_york
print("NY:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))        #in ra man hinh ngay-gio

tz_London = pytz.timezone('Europe/London')      #chuyen doi mui gio, Time zone argument is London
datetime_London = datetime_NY.now(tz_London)       #tra ve ngay-gio hien tai cua New_york
print("London:", datetime_London.strftime("%m/%d/%Y, %H:%M:%S"))    #in ra man hinh ngay-gio