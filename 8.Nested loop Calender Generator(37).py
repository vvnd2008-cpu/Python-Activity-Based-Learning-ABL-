# Nested Loop Calendar Generator
import calendar
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))
if month < 1 or month > 12 or year <= 0:
    print("Invalid month or year.")
else:
    print(f"\n{calendar.month_name[month]} {year}")
    print("Mo Tu We Th Fr Sa Su")

    weeks = calendar.monthcalendar(year, month)

    for week in weeks:
        for day in week:
            if day == 0:
                print(" ", end="")
            else:
                print(f"{day:2} ", end="")
        print()
