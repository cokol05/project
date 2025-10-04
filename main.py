lst = [x**2 for x in range(1, 11)]
print(*lst)

nums = [x for x in range(1, 20) if x % 2 == 0]
print(*nums)

words = ["python", "Java", "c++", "Rust", "go"]
new_words = [word.upper() for word in words if len(word) > 3]
print(*new_words)


class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


for x in Countdown(5):
    print(x, end=' ')
print()

def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(5):
    print(num, end=' ')

print()


from decimal import Decimal


p = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
r = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
t = Decimal(input("Введите срок вклада (в годах): "))

res = (p * (Decimal('1') + r / (Decimal('12') * Decimal('100'))) ** (Decimal('12') * t)).quantize(Decimal('0.01'))

print(f"Итоговая сумма: {res} руб.")
print(f"Общая прибыль: {res - p} руб.")
print()


from fractions import Fraction


frac1 = Fraction(3, 4)
frac2 = Fraction(5, 6)

print(f"Сложение: {frac1} + {frac2} = {frac1 + frac2}")
print(f"Вычитание: {frac1} - {frac2} = {frac1 - frac2}")
print(f"Умножение: {frac1} * {frac2} = {frac1 * frac2}")
print(f"Деление: {frac1} / {frac2} = {frac1 / frac2}")
print()


from datetime import datetime


current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

current_date = current_datetime.date()
print("Текущая дата:", current_date)

current_time = current_datetime.time()
print("Текущее время:", current_time)


from datetime import date, datetime


birthday = date(2006, 1, 19)
today = date.today()

deltaday = (today - birthday).days

next_birthday = date(today.year, birthday.month, birthday.day)

if today > next_birthday:
    next_birthday = date(today.year + 1, birthday.month, birthday.day)

days_next_dr = (next_birthday - today).days

print(f"Дней прошло с момента рождения: {deltaday:,}")
print(f"Дней до следующего дня рождения: {days_next_dr:,}")
print()


from datetime import datetime


def curdata(dt):
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }

    return f"Сегодня {dt.day} {months[dt.month]} {dt.year} года, время: {dt:%H:%M}"


print(curdata(datetime.now()))
