def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def find_leap_years(start, end):
    leap_years = []
    for year in range(start, end + 1):
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years

start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

leap_years = find_leap_years(start_year, end_year)

if len(leap_years) > 0:
    print(f"The leap years between {start_year} and {end_year} are:")
    for year in leap_years:
        print(year)
else:
    print(f"There are no leap years between {start_year} and {end_year}.")
