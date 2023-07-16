import pandas as pd
import os

data = pd.read_csv('coindesk.csv')

df = pd.DataFrame(data)

# Получаем путь к текущей директории
current_directory = os.getcwd()

# Создаем новую директорию
directory = os.path.join(current_directory, 'directory')
os.makedirs(directory, exist_ok=True)

# Сохраняем DataFrame в CSV-файл в новой директории
csv_file = os.path.join(directory, 'filename.csv')
df.to_csv(csv_file, index=False)

# Сохраняем DataFrame в Excel-файл в новой директории
excel_file = os.path.join(directory, 'filename.xlsx')
df.to_excel(excel_file, index=False)

# Сохраняем DataFrame в JSON-файл в новой директории
json_file = os.path.join(directory, 'filename.json')
df.to_json(json_file)

# Проверяем существование и загружаем CSV-файл, если он есть
if os.path.exists(csv_file):
    df_csv = pd.read_csv(csv_file)
    print('\nInfo from csv_file: ')
    print(df_csv)
else:
    print('\nФайл не найден ')

# Проверяем существование и загружаем excel-файл, если он есть
if os.path.exists(excel_file):
    df_excel = pd.read_excel(excel_file)
    print('\nInfo from excel_file: ')
    print(df_excel)
else:
    print('\nФайл не найден ')

# Проверяем существование и загружаем json-файл, если он есть
if os.path.exists(json_file):
    df_json = pd.read_json(json_file)
    print('\nInfo from json_file: ')
    print(df_json)
else:
    print('\nФайл не найден ')