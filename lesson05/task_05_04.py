"""4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл. """
import googletrans
from googletrans import Translator


try:
    filename_inp = r"txt\task_05_04.txt"
    f_out = open(r"txt\task_05_04_out.txt", "w", encoding="utf-8")
    with open(filename_inp, "r", encoding="utf-8") as f_cool:
        for i in f_cool:
            translator = Translator()
            result = translator.translate(i, src='en', dest='ru')
            print(result.text, file=f_out)
except IOError:
    print("Такого файла не существует")
finally:
    f_out.close()
