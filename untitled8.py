import datetime as dt
text="10.10.2019 10:22:13"
print(dt.datetime.strptime(text,"%d.%m.%Y %H:%M:%S"))