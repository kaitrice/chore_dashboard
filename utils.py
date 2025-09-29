from datetime import datetime


def isSunday():
    today = datetime.today()
    day_of_the_week = today.weekday()
    return day_of_the_week == 6