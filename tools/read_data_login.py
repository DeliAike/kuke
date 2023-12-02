import json

from tools.file_base_path import BASE_PATH

list_login = []
with open(BASE_PATH + 'updata.json', 'r', encoding='utf-8') as f:
    login_data = json.load(f)

    # print(login_data[0])
for data in login_data:
    user_tel = data['user']
    password = data['password']
    expect = data['expect']
    list_login.append((user_tel, password))
print(list_login)