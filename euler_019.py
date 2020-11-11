
import calendar

sum = 0

c = calendar.TextCalendar(0)

for year in range(1901, 2001):
	for month in range(1, 13):
		if c.monthdayscalendar(year, month)[0][6] == 1:
			sum += 1

print(sum)


