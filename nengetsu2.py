
import calendar
def calendar2():
    year = int(input("今日は何年？"))
    mon = int(input("今日は何月？"))
    return(calendar.month(year,mon))
a = calendar2()
print(a)

