from classes import Note
import random
from classes import Note
import json

def main_menu() -> int:
    user_choice = input("\nПриложение 'Заметки'. Главное меню." \
    + "\n\n" \
    + "1. Создать заметку;"
    "\n2. Редактировать заметку;"
    "\n3. Посмотреть список заметок;"
    "\n4. Удалить заметку;"
    "\n5. Вернуться в Главное меню."
    "\n\nВыберите действие (1-5): ")

    while not (user_choice.isdigit() and int(user_choice) in [1, 2, 3, 4, 5]):
        user_choice = input("\nОшибка! Введите число от 1 до 5 для выбора действия:" \
                            + "\n\n" \
                            + "1. Создать заметку;"
                            "\n2. Редактировать заметку;"
                            "\n3. Посмотреть список заметок;"
                            "\n4. Удалить заметку;"
                            "\n5. Вернуться в Главное меню."
                            "\n\nВыберите действие (1-5): ")

    return int(user_choice)

def write_id_to_file(path, id):
  with open(path, 'a') as file:
      file.write(str(id) + '\n')

def read_ids_from_file(path):
  ids_list = []
  test_str = ''
  with open(path, 'r') as file:
    for line in file.readlines():
      test_str += line
  ids_list = test_str.split('\n')

  return ids_list

def generate_unique_id(ids_list):
  unique_id = random.randint(1, 100)
  while unique_id in ids_list:
    unique_id = random.randint(1, 100)
  
  return unique_id

def read_json_notes():
  notes_list = []
  with open ('json_notes.json', 'r') as json_file:
    data = json.load(json_file)

    for note in data:
      print('note_id: ' + note['note_id'])
      print('note_header: ' + note['note_header'])
      print('note_body: ' + note['note_body'])
      print('note_date: ' + note['note_date'])
      print('')
      notes_list.append(note)
    
  return notes_list

def note_choice(ids_list):
  user_choice = input("Введите id заметки, подлежащей изменению: ")
  while not (user_choice.isdigit() and (user_choice in ids_list)):
    user_choice = input("Ошибка ввода! Введите id заметки, подлежащей изменению: ")
  