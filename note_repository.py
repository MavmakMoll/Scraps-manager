
import json

from models import Note, TextNote, Task, Recipe


class NoteRepository:
    def __init__(self, file_path: str = "notes.json"):
        self.notes: list[Note] = []
        self.file_path = file_path

    def save_notes(self, next_id: int) -> None:
        data = {
            "next_id": next_id,
            "notes": [
                note.to_dict() for note in self.notes
            ]
        }

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

        except OSError as error:
            raise RuntimeError(
                f"Не удалось сохранить заметки: {error}"
            ) from error

    def add_note(self, note: Note) -> None:
        self.notes.append(note)

    def remove_note(self, note: Note) -> None:
        self.notes.remove(note)

    def get_all_notes(self) -> list[Note]:
        return self.notes.copy()

    def load_notes(self) -> int:
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

        except FileNotFoundError:
            self.notes = []
            return 1

        except json.JSONDecodeError as error:
            raise ValueError(
                "Файл заметок содержит некорректный JSON"
            ) from error

        except OSError as error:
            raise RuntimeError(
                f"Не удалось прочитать файл заметок: {error}"
            ) from error

        if not isinstance(data, dict):
            raise ValueError("Некорректная структура файла заметок")

        next_id = data.get("next_id")
        notes_data = data.get("notes")

        if (
            not isinstance(next_id, int)
            or isinstance(next_id, bool)
            or next_id < 1
        ):
            raise ValueError("Некорректное значение next_id")

        if not isinstance(notes_data, list):
            raise ValueError("Поле notes должно быть списком")

        loaded_notes = []

        for note_data in notes_data:
            if not isinstance(note_data, dict):
                raise ValueError("Некорректная структура заметки")

            note_type = note_data.get("type")

            try:
                note_id = note_data["id"]
                title = note_data["title"]

                if (
                    not isinstance(note_id, int)
                    or isinstance(note_id, bool)
                    or note_id < 1
                ):
                    raise ValueError("Некорректный ID заметки")

                if not isinstance(title, str) or not title.strip():
                    raise ValueError("Некорректный заголовок заметки")

                if note_type == "text":
                    content = note_data["content"]

                    if not isinstance(content, str):
                        raise ValueError("Содержание должно быть строкой")

                    note = TextNote(note_id, title, content)

                elif note_type == "task":
                    content = note_data["content"]
                    days_left = note_data["days_left"]

                    if not isinstance(content, str):
                        raise ValueError("Содержание должно быть строкой")

                    if (
                        not isinstance(days_left, int)
                        or isinstance(days_left, bool)
                        or days_left < 0
                    ):
                        raise ValueError("Некорректное количество дней")

                    note = Task(note_id, title, content, days_left)

                elif note_type == "recipe":
                    steps = note_data["steps"]

                    if (
                        not isinstance(steps, list)
                        or not all(isinstance(step, str) for step in steps)
                    ):
                        raise ValueError("Некорректный список шагов рецепта")

                    note = Recipe(note_id, title, steps)

                else:
                    raise ValueError(
                        f"Неизвестный тип заметки: {note_type}"
                    )

            except KeyError as error:
                raise ValueError(
                    f"В заметке отсутствует обязательное поле: {error}"
                ) from error

            loaded_notes.append(note)

        ids = [note.id for note in loaded_notes]

        if len(ids) != len(set(ids)):
            raise ValueError("Обнаружены повторяющиеся ID заметок")

        if loaded_notes and next_id <= max(ids):
            raise ValueError(
                "next_id должен быть больше всех существующих ID"
            )

        self.notes = loaded_notes

        return next_id
