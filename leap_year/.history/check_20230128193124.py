def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("leap year")
            else:
                return ("not leap year")
        else:
            return ("leap year")
    else:
        return ("not leap year")

is_leap_year(2002)