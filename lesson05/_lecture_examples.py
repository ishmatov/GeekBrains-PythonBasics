f_cool = open(r"txt\text_3.txt", "r", encoding="utf-8")
content_read = f_cool.read()
print(content_read)
f_cool.close()

print()
f_cool = open(r"txt\text_3.txt", "r", encoding="utf-8")
content_readline = f_cool.readline()
print(content_readline, end="")
content_readline = f_cool.readline()
print(content_readline, end="")
f_cool.close()

print()
f_cool = open(r"txt\text_3.txt", "r", encoding="utf-8")
content_readlines = f_cool.readlines()
print(content_readlines)
f_cool.close()

# Перебор циклом не программно
print()
f_cool = open(r"txt\text_3.txt", "r", encoding="utf-8")
for i in f_cool:
    print(i, end="")
f_cool.close()

# Выгрузка определенного объема в байтах")
print("\n\n")
f_cool = open(r"txt\text_3.txt", "r", encoding="utf-8")
content_byte = f_cool.read(10)
print(content_byte)
f_cool.close()

# ------------------------------------- Запись в файл ---------------------------------------------------------------
# Создать пустой файл
f_cool = open(r"txt\text_33.txt", "w", encoding="utf-8")
f_cool.close()

# Запись строки
f_cool = open(r"txt\text_33.txt", "w", encoding="utf-8")
f_cool.write("Python1\nPython2\n")
f_cool.close()

# Запись списка
f_cool = open(r"txt\text_33.txt", "w", encoding="utf-8")
f_cool.writelines(["Python1\n", "Python2\n"])
f_cool.close()

# ------------------------------------- Менеджер контекста ----------------------------------------------------------
# Не нужно закрывать файл
with open(r"txt\text_33.txt", "r", encoding="utf-8") as f_cool:
    for i in f_cool:
        print(i)

# -------------------------------------- Ловим ошибки ---------------------------------------------------------------
try:
    with open(r"txt\text_3333.txt", "r", encoding="utf-8") as f_cool:
        for i in f_cool:
            print(i)
except IOError:
    print("IOError - Такого файла не существует")

# -------------------------------------- Режимы открытия файла ------------------------------------------------------
# x - создаст файл и откроет его для записи, только в том случае если его ещё нет
# Если файл существует то будет ошибка FileExistsError
try:
    with open(r"txt\text_33.txt", "x", encoding="utf-8") as f_cool:
        pass # заглушка
except FileExistsError:
    print("FileExistsError - Такой файл уже существует")

# a - откроет файл для дозаписи, если его не существует, то создаст новый
with open(r"txt\text_a.txt", "a", encoding="utf-8") as f_cool:
    f_cool.write("\nPython")

# r+ - откроет файл для чтения и для записи, если его не существует, то ошибка
try:
    with open(r"txt\text_r_plus.txt", "r+", encoding="utf-8") as f_cool:
        print(f_cool.read())
        f_cool.write("\nPython")
except IOError:
    print("Такого файла не существует")

# a+ открытие для чтения и для дозаписи. Чтобы считать данные нужно поднять каретку
# Если файла нет, то создаёт его
with open(r"txt\text_a_plus.txt", "a+", encoding="utf-8") as f_cool:
    f_cool.write("\nPython - a+")
    f_cool.seek(0) #Позволяет выполнить переход на нужную позицию
    print(f_cool.read())

try:
    with open(r"txt\text_r_plus.txt", "r", encoding="utf-8") as f_cool:
        print(f_cool.read(8)) #Считывает определённое кол-во байт
        print(f"Позиция курсора - {f_cool.tell()}")
except IOError:
    print("Такого файла не существует")


try:
    with open(r"txt\text_33.txt", "r", encoding="utf-8") as f_cool:
        print(f"Закрыт ли файл - {f_cool.closed}")
        print(f"Режим доступа к файлу - {f_cool.mode}")
        print(f"Имя файла - {f_cool.name}")
except IOError:
    print("Такого файла не существует")

# -------------------------------------- Запись в файл с помощью print -----------------------------------------------
with open(r"txt\text_print.txt", "w", encoding="utf-8") as f_cool:
    print("Hello, People", file=f_cool)
