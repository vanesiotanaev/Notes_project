import model
import random
from datetime import datetime
from classes import Note
import time

def button():
    path_ids = 'path_ids.txt'
    action = model.main_menu()

    if action == 1:
        try:
            ids_list = model.read_ids_from_file(path_ids)
            unique_id = model.generate_unique_id(ids_list)
            model.write_id_to_file(path_ids, unique_id)
            print(model.read_ids_from_file(path_ids))
        except:
            unique_id = random.randint(1, 100)
            model.write_id_to_file(path_ids, unique_id)
        
        note_header = input("Введите заголовок заметки: ")
        note_body = input("Введите текст заметки: ")
        note_date = str(datetime.now().date())
        note = Note(note_id=unique_id, note_header=note_header, note_body=note_body, note_date=note_date)
        # note.show_object()
        try:
            notes_list = model.read_json_notes()
        except:
            notes_list = []
        note.add_note_to_json(notes_list)
        time.sleep(1)
        print("Заметка успешно добавлена!")
        time.sleep(1)
    
    if action == 2:
        # try:
            notes_list = model.read_json_notes()
            ids_list = model.read_ids_from_file(path_ids)
            note_choice = model.note_choice(ids_list)
            print(model.read_json_notes())
        # except:
        #     time.sleep(1)
        #     print('')
        #     print('Заметок нет!')
        #     time.sleep(1)

