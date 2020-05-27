"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text):
    text_list = list(text)
    text_list[0] = text_list[0].upper()
    return "".join(text_list)


def check_txt(text):
    for el in list(text):
        if 97 > ord(el) < 122:
            return False
    return True


while True:
    text = input("Введите слово из маленьких латинских букв ")
    if check_txt(text):
        print(int_func(text))
        break

text = input("Введите слова разделенный пробелом ")
text_list = text.split()
result = ""
for el in text.split():
    result += int_func(el) + " "

print(result)
