"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""
str = input("Введите строку из нескольких слов разделённых пробелами: ")
i = 1
str_list = str.split()
for el in str_list:
    print(f"{i} - {el[:10]}")
    i += 1
