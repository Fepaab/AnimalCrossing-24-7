import datetime

def nowplaying():
    YEAR = datetime.date.today().year
    MONTH = datetime.date.today().month
    DATE = datetime.date.today().day
    HOUR = datetime.datetime.now().hour
    MINUTE = datetime.datetime.now().minute
    SECONDS = datetime.datetime.now().second

    if HOUR == 0:
        hour_12 = 12
        ampm = "am"
    elif HOUR < 12:
        hour_12 = HOUR
        ampm = "am"
    elif HOUR == 12:
        hour_12 = 12
        ampm = "P.M."
    else:
        hour_12 = HOUR - 12
        ampm = "P.M."
    return f'Now Playing: {hour_12} {ampm} from Animal Crossing (Original From Gamecube)'

def horario():
    YEAR = datetime.date.today().year
    MONTH = datetime.date.today().month
    DATE = datetime.date.today().day
    HOUR = datetime.datetime.now().hour
    MINUTE = datetime.datetime.now().minute
    SECONDS = datetime.datetime.now().second
    return f'{YEAR:02d}-{MONTH:02d}-{DATE:02d} {HOUR:02d}:{MINUTE:02d}:{SECONDS:02d}'

def meridiantime():
    HOUR = datetime.datetime.now().hour
    if HOUR == 0:
        hour_12 = 12
        ampm = "am"
    elif HOUR < 12:
        hour_12 = HOUR
        ampm = "am"
    elif HOUR == 12:
        hour_12 = 12
        ampm = "pm"
    else:
        hour_12 = HOUR - 12
        ampm = "pm"
    return f'{hour_12}_{ampm}'
