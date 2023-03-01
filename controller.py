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
        except:
            unique_id = 1
            model.write_id_to_file(path_ids, unique_id)
        
        note_header = input("Введите заголовок заметки: ")
        note_body = input("Введите текст заметки: ")
        note_date = str(datetime.now().date())
        note = Note(note_id=unique_id, note_header=note_header, note_body=note_body, note_date=note_date)
        try:
            notes_list = model.read_json_notes_as_list()
        except:
            notes_list = []
        note.add_note_to_json(notes_list)
        time.sleep(1)
        print("Заметка успешно добавлена!")
        time.sleep(1)
    
    if action == 2:
        try:
            notes_list = model.read_json_notes_as_list()
            ids_list = model.read_ids_from_file(path_ids)
            model.show_json_notes()
            note_choice = model.note_choice(ids_list)
            new_header = input('Введите новый заголовок заметки: ')
            new_body = input('Введите новый текст заметки: ')
            new_date = str(datetime.now().date())
            # note = Note(note_id=note_choice, note_header=new_header, note_body=new_body, note_date=new_date)
            notes_list = model.header_edit(note_choice, notes_list, new_header)
            notes_list = model.body_edit(note_choice, notes_list, new_body)
            model.edit_json_note(note_choice, new_header, new_body, new_date)
        except:
            time.sleep(1)
            print('')
            print('Заметок нет!')
            time.sleep(1)
    
    if action == 3:
        model.show_json_notes()
    
    if action == 4:
        try:
            if len(model.read_json_notes_as_list()) == 0:
                time.sleep(1)
                print('')
                print('Заметок нет!')
                time.sleep(1)
            else:
                ids_list = model.read_ids_from_file(path_ids)
                model.show_json_notes()
                note_choice = model.note_choice(ids_list)
                model.delete_json_note(note_choice)
                ids_list.remove(note_choice)
                model.update_ids_file(path_ids, ids_list)
        except:
            time.sleep(1)
            print('')
            print('Заметок нет!')
            time.sleep(1)
    
    if action == 5:
        model.choose_note_by_date()
