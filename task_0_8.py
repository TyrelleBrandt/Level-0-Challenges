def hours_and_minutes(number):
    range = str(1)
    hours = str(number // 60)
    minutes = str(number % 60)
    if hours == range and minutes == range:
        print(hours, "hour" + ", " + minutes, "minute")
    elif hours > range and minutes > range:
        print(hours, "hours" + ", " + minutes, "minutes")
    elif hours == range and minutes > range:
        print(hours, "hour" + ", " + minutes, "minutes")
    elif hours > range and minutes == range:
        print(hours, "hours" + ", " + minutes, "minute")


hours_and_minutes(71)
