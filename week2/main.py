import dow
dow.makeCalendar()
def getDayOfTheWeekForUserDate():

    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))

    weekdays = ["Saturday", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday"]

    weekday = dow.getDayOfTheWeek(year, month, day)

    print(weekdays[weekday])


getDayOfTheWeekForUserDate()