"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
timeInSec = int(input("Enter time in seconds: "))
hours = timeInSec // 3600
minutes = (timeInSec - (hours * 3600)) // 60
seconds = timeInSec % 60
print(f"{timeInSec} sec = {hours:02}:{minutes:02}:{seconds:02}")
