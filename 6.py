from decimal import Decimal


p = Decimal(input("Введите начальную сумму вклада (рубли.копейки): "))
r = Decimal(input("Введите годовую процентную ставку (например, 7.5): "))
t = Decimal(input("Введите срок вклада (в годах): "))

res = (p * (Decimal('1') + r / (Decimal('12') * Decimal('100'))) ** (Decimal('12') * t)).quantize(Decimal('0.01'))

print(f"Итоговая сумма: {res} руб.")
print(f"Общая прибыль: {res - p} руб.")
