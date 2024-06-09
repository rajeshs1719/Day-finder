import difflib

Odd_days = {
    "1": 3,
    "2": [0, 1],  
    "3": 3,
    "4": 2,
    "5": 3,
    "6": 2,
    "7": 3,
    "8": 3,
    "9": 2,
    "10": 3,
    "11": 2,
    "12": 3
}

Years_no = {
    '1600': 0,
    '1700': 5,
    '1800': 3,
    '1900': 1
}

def traverse_year(Year):
    cal_year = difflib.get_close_matches(Year[0:2] + "00", Years_no.keys())
    if not cal_year:
        reduced_year = str(int(Year) - 400)
        cal_year = difflib.get_close_matches(reduced_year[0:2] + "00", Years_no.keys())
        if not cal_year:
            return None
    cal_year = str(cal_year[0])
    year = str(int(Year) - 1)
    year_calculate = Years_no[cal_year] + (int(year[2:])) // 4 * 2 + (int(year[2:]) - int(year[2:]) // 4)
    return year_calculate

def is_leap_year(Year):
    year = int(Year)
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_day(Date, Month, Year):
    year_calculate = traverse_year(Year)
    if year_calculate is None:
        print("Year out of supported range.")
        return

    sum_odd_days = 0
    leap_year = is_leap_year(Year)

    for i in range(1, int(Month)):
        if str(i) == "2":  # February
            sum_odd_days += Odd_days[str(i)][1] if leap_year else Odd_days[str(i)][0]
        else:
            sum_odd_days += Odd_days[str(i)]

    day_finder = (year_calculate + sum_odd_days + Date) % 7
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(days_of_week[day_finder])

def validate_date(Date, Month, Year):
    if int(Year) < 1600 or int(Year) > 2300:
        print("Year out of range. Enter a year between 1600 and 2300.")
        return False
    if int(Month) < 1 or int(Month) > 12:
        print("Month out of range. Enter a month between 1 and 12.")
        return False
    if Month == '2':
        if is_leap_year(Year):
            if Date < 1 or Date > 29:
                print("Invalid date for February in a leap year. Enter a date between 1 and 29.")
                return False
        else:
            if Date < 1 or Date > 28:
                print("Invalid date for February. Enter a date between 1 and 28.")
                return False
    elif Date < 1 or Date > 31:
        print("Date out of range. Enter a date between 1 and 31.")
        return False
    return True

Date = int(input("Enter the date="))
Month = input("Enter the month=")
Year = input("Enter the year=")

if validate_date(Date, Month, Year):
    find_day(Date, Month, Year)