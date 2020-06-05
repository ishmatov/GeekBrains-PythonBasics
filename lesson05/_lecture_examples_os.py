import os

print("Создаём файл")
f_cool = open(r"txt\text_for_remove.txt", "w", encoding="utf-8")
f_cool.close()

print("Удаляем файл")
os.remove(r"txt\text_for_remove.txt")

print("Создаём файл")
f_cool = open(r"txt\text_for_rename.txt", "w", encoding="utf-8")
f_cool.close()

print("Переименовываем файл")
os.rename(r"txt\text_for_rename.txt", r"txt\text_after_rename.txt")

print("Удаляем файл")
os.remove(r"txt\text_after_rename.txt")

print(os.listdir())