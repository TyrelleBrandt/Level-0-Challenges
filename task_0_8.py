def hours_and_minutes(number):
    range = str(0)
    hours = str(number // 60)
    minutes = str(number % 60)
    if hours == range and minutes == range:
        print(f"{hours} hours, {minutes} minutes")
    elif hours > range and minutes > range:
        print(f"{hours} hours, {minutes} minutes")
    elif hours == range and minutes > range:
        print(f"{hours} hour, {minutes} minutes")
    elif hours > range and minutes == range:
        print(f"{hours} hours, {minutes} minute")


hours_and_minutes(700)
