from datetime import date, datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthday_dict = defaultdict(list)
    date_today = date.today()
    
    for user in users:
        if user["birthday"] < date_today:
            next_birthday = user["birthday"].replace(year=date_today.year + 1)
        else:
            next_birthday = user["birthday"]
     
        days_until_birthday = (next_birthday - date_today).days
        full_day_name = next_birthday.strftime("%A")

        if 0 <= days_until_birthday < 7:
            if full_day_name == "Saturday" or full_day_name == 'Sunday':
                birthday_dict["Monday"].append(user["name"])
            else:
                birthday_dict[full_day_name].append(user["name"])

    return birthday_dict

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 12, 2).date()},
        {"name": "Bill Gates", "birthday": datetime(2023, 12, 3).date()},
        {"name": "Mark Zuckerberg", "birthday": datetime(2023, 12, 4).date()},
        {"name": "Elon Musk", "birthday": datetime(2023, 12, 5).date()},
        {"name": "Tim Cook", "birthday": datetime(2023, 12, 6).date()},
        {"name": "Satya Nadella", "birthday": datetime(2023, 12, 7).date()},
        {"name": "Sheryl Sandberg", "birthday": datetime(2023, 12, 8).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)