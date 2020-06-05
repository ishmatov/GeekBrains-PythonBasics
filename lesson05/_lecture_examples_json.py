import json

data = {
    "income": {
        "salary": 50000,
        "bonus": 20000
    }
}

# Преобразование из Python в json с записью в файл
with open(r"txt\m_j.json", "w", encoding="utf-8") as f_cool:
    json.dump(data, f_cool)

# Преобразование данных без создания файла
json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# Преобразование из json файла в Python
with open(r"txt\m_j.json", "r", encoding="utf-8") as f_cool:
    dataa = json.load(f_cool)
print(dataa)
print(type(dataa))

# Преобразование из json строки в Python
data_from_str_json = json.loads(json_str)
print(data_from_str_json)
print(type(data_from_str_json))