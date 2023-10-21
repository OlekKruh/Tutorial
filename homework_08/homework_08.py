from datetime import datetime, date, timedelta


def get_birthdays_per_week(users):
    # Variables
    result = {}

    # Determining today's date and next Sunday's date
    today = date.today()
    day_of_week = today.weekday()
    day_of_week_writen = today.strftime('%A')

    # Definitions of the previous Friday
    if day_of_week == 4:
        previous_friday = today
    else:
        days_until_previous_friday = (day_of_week + 7 - 4) % 7
        previous_friday = today - timedelta(days=days_until_previous_friday)

    # Definitions of the next Friday
    days_until_next_friday = (4 - day_of_week + 7) % 7
    next_friday = today + timedelta(days=days_until_next_friday)

    print(f'Today date: {today}')
    print(f'Day of week: {day_of_week_writen}')
    print(f'Days until next friday: {days_until_next_friday}')
    print(f'Previous friday: {previous_friday}')
    print(f'Next friday: {next_friday}')

    # If users list is empty
    if len(users) == 0:
        return result

    # if users list is not empty
    for user in users:
        name = user['name']
        birthday = user['birthday']

        if (previous_friday.month, previous_friday.day) < (birthday.month, birthday.day) <= (
                next_friday.month, next_friday.day):
            birthday = birthday.replace(year=today.year)
            day = birthday.strftime('%A')

            if day == 'Sunday' or day == 'Saturday':
                day = 'Monday'
            if day not in result:
                result[day] = []
            result[day].append(name)

    return result


if __name__ == "__main__":
    users = [
        {'name': 'Person_1', 'birthday': datetime(2000, 10, 25).date()},
        {'name': 'Person_2', 'birthday': datetime(1995, 10, 26).date()},
        {'name': 'Person_3', 'birthday': datetime(1985, 10, 27).date()},
        {'name': 'Person_4', 'birthday': datetime(1978, 10, 28).date()},
        {'name': 'Person_5', 'birthday': datetime(1982, 10, 29).date()},
        {'name': 'Person_6', 'birthday': datetime(1990, 10, 30).date()},
        {'name': 'Person_7', 'birthday': datetime(2003, 10, 31).date()},
        {'name': 'Person_8', 'birthday': datetime(2007, 10, 25).date()},
        {'name': 'Person_9', 'birthday': datetime(1999, 10, 26).date()},
        {'name': 'Person_10', 'birthday': datetime(1993, 10, 27).date()},
        {'name': 'Person_11', 'birthday': datetime(1990, 11, 1).date()},
        {'name': 'Person_12', 'birthday': datetime(1985, 11, 2).date()},
        {'name': 'Person_13', 'birthday': datetime(1978, 11, 3).date()},
        {'name': 'Person_14', 'birthday': datetime(2002, 11, 4).date()},
        {'name': 'Person_15', 'birthday': datetime(1982, 11, 5).date()},
        {'name': 'Person_16', 'birthday': datetime(2000, 11, 6).date()},
        {'name': 'Person_17', 'birthday': datetime(1995, 11, 7).date()},
        {'name': 'Person_18', 'birthday': datetime(1999, 11, 8).date()},
        {'name': 'Person_19', 'birthday': datetime(1993, 11, 1).date()},
        {'name': 'Person_20', 'birthday': datetime(2005, 11, 2).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
