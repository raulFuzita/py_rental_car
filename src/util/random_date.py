from datetime import date

def add_years(d: date, years: int) -> date:
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

def sub_years(d: date, years: int) -> date:
    try:
        return d.replace(year = d.year - years)
    except ValueError:
        return d + (date(d.year - years, 1, 1) - date(d.year, 1, 1))

def rand_date(stop: int=0, *, start: int=0, initial_date: date=date.today()) -> date:
    newdate = sub_years(initial_date, start)
    return add_years(newdate, stop)

