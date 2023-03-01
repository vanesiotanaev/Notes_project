import json

class Note:
    note_id: int
    note_header: str
    note_body: str
    note_date: str

    def __init__(self, note_id: int, note_header: str, note_body: str, note_date: str):
        self.note_id = note_id
        self.note_header = note_header
        self.note_body = note_body
        self.note_date = note_date
    
    def show_object(self):
        print(self.note_id)
        print(self.note_header)
        print(self.note_body)
        print(self.note_date)
    
    def add_note_to_json(self, notes_list):
        data = {'note_id': str(self.note_id),
                'note_header': self.note_header,
                'note_body': self.note_body,
                'note_date': self.note_date}
        notes_list.append(data)
        
        with open('json_notes.json', 'w') as outfile:
            json.dump(notes_list, outfile)