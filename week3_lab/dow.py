def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def getDayOfTheWeek(year, month, day):

    last_two_digits = year % 100

    how_many_twelves = last_two_digits // 12

    remainder = last_two_digits % 12

    how_many_fours = remainder // 4
    if month == 1:
        month_code = 1

    elif month == 2:
        month_code = 4

    elif month == 3:
        month_code = 4

    elif month == 4:
        month_code = 0

    elif month == 5:
        month_code = 2

    elif month == 6:
        month_code = 5

    elif month == 7:
        month_code = 0

    elif month == 8:
        month_code = 3

    elif month == 9:
        month_code = 6

    elif month == 10:
        month_code = 1

    elif month == 11:
        month_code = 4

    elif month == 12:
        month_code = 6
    is_leap = isLeapYear(year)
    total = how_many_twelves + remainder + how_many_fours + day + month_code

    if is_leap and (month == 1 or month == 2):
        total = total - 1
    if year >= 1600 and year < 1700:
        total = total + 6
    elif year >= 1700 and year < 1800:
        total = total + 4
    elif year >= 1800 and year < 1900:
        total = total + 2

    weekday = total % 7

    return weekday

def makeCalendar():
   for month in range(1, 13):
           if month == 1:
               days_in_month = 31
           elif month == 2:
               days_in_month = 28
           elif month ==3:
               days_in_month = 31
           elif month ==4:
               days_in_month = 30
           elif month ==5:
               days_in_month = 31
           elif month ==6:
               days_in_month = 30
           elif month ==7:
               days_in_month = 31
           elif month ==8:
               days_in_month = 31
           elif month ==9:
               days_in_month = 30
           elif month ==10:
               days_in_month = 31
           elif month ==11:
               days_in_month = 30
           elif month ==12:
               days_in_month = 31
           weekdays = ["Saturday", "Sunday", "Monday", "Tuesday",
                          "Wednesday", "Thursday", "Friday"]
           for day in range(1, days_in_month + 1):
               weekday = getDayOfTheWeek(2026, month, day)
               weekday_name = weekdays[weekday]
               print(f"{month}-{day}-2026 is a {weekday_name.lower()}.")
# makeCalendar()








