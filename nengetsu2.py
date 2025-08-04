
import calendar
def main():
    year = int(input("今日は何年？"))
    mon = int(input("今日は何月？"))
    return(calendar.month(year,mon))
if __name__ == "__main__":
    a = main()
    print(a)

