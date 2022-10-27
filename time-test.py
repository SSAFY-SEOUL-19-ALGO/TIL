from datetime import datetime, date, timezone, timedelta

now = datetime.now()


updateTime = now.strftime('%Y-%m-%d %H:%M:%S %z')

print(updateTime)
