from datetime import datetime, date


birthday = date(2006, 1, 19)
today = date.today()

deltaday = (today - birthday).days

next_birthday = date(today.year, birthday.month, birthday.day)

if today > next_birthday:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_next_dr = (next_birthday - today).days

print(f"Дней прошло с момента рождения: {deltaday:,}")
print(f"Дней до следующего дня рождения: {days_next_dr:,}")
