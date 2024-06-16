#s24004
#現在時刻と2024/6カレンダーを表示

import datetime
import calendar

nowtime = datetime.datetime.now()
print(nowtime.strftime("%Y年%m月%d日 %H:%M:%S"))

print(calendar.month(2024, 6))
