from datetime import datetime, date


current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

current_date = current_datetime.date()
print("Текущая дата:", current_date)

current_time = current_datetime.time()
print("Текущее время:", current_time)
