import json

from models import Note, TextNote, Task, Recipe


class NoteRepository:
    def __init__(self):
        self.notes: list[Note] = []
        self.file_path = "notes.json"

    def save_notes(self, next_id: int) -> None:
        data = {
            "next_id": next_id,
            "notes": [
                note.to_dict() for note in self.notes
            ]
        }

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def remove_note(self, note: Note) -> None:
        self.notes.remove(note)

    def get_all_notes(self) -> list[Note]:
        return self.notes

    def load_notes(self) -> int:
        with open(self.file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.notes = []

        for note_data in data["notes"]:
            note_type = note_data["type"]

            if note_type == "text":
                note = TextNote(
                    note_data["id"],
                    note_data["title"],
                    note_data["content"]
                )

            elif note_type == "task":
                note = Task(
                    note_data["id"],
                    note_data["title"],
                    note_data["content"],
                    note_data["days_left"]
                )

            elif note_type == "recipe":
                note = Recipe(
                    note_data["id"],
                    note_data["title"],
                    note_data["steps"]
                )

            else:
                raise ValueError(f"Неизвестный тип заметки: {note_type}")

            self.notes.append(note)

        return data["next_id"]