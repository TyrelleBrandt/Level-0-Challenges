def hours_and_minutes(number):
    a = str(1)
    hours = str(number // 60)
    minutes = str(number % 60)
    if hours == a and minutes == a:
        print(hours, "hour" + ", " + minutes, "minute")
    elif hours > a and minutes > a:
        print(hours, "hours" + ", " + minutes, "minutes")
    elif hours == a and minutes > a:
        print(hours, "hour" + ", " + minutes, "minutes")
    elif hours > a and minutes == a:
        print(hours, "hours" + ", " + minutes, "minute")


hours_and_minutes(71)
