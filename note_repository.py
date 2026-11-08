from models import Note

class NoteRepository:
    def __init__(self):
        self.notes: list[Note] = []
        self.file_path: str = "notes.json"


    def save_notes(self) -> None:
        pass

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def remove_note(self, note: Note) -> None:
        self.notes.remove(note)

    def get_all_notes(self) -> list[Note]:
        return self.notes

    def load_notes(self) -> None:
        pass
