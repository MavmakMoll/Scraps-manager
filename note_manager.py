
from models import Note, TextNote, Task, Recipe
from note_repository import NoteRepository


class NoteManager:
    def __init__(self, repository: NoteRepository):
        self.repository = repository
        self.next_id = self.repository.load_notes()

    def _validate_title(self, title: str) -> str:
        title = title.strip()

        if not title:
            raise ValueError("Заголовок не может быть пустым")

        for note in self.repository.get_all_notes():
            if note.title.casefold() == title.casefold():
                raise ValueError("Заметка с таким заголовком уже существует")

        return title

    def _add_note(self, note: Note) -> None:
        self.repository.add_note(note)

        self.repository.save_notes(self.next_id + 1)

        self.next_id += 1

    def create_text_note(self, title: str, content: str) -> TextNote:
        title = self._validate_title(title)

        note = TextNote(
            self.next_id,
            title,
            content
        )

        self._add_note(note)

        return note

    def create_task(
        self,
        title: str,
        content: str,
        days_left: int
    ) -> Task:
        title = self._validate_title(title)

        if not isinstance(days_left, int) or isinstance(days_left, bool):
            raise ValueError("Количество дней должно быть целым числом")

        if days_left < 0:
            raise ValueError("Количество дней не может быть отрицательным")

        note = Task(
            self.next_id,
            title,
            content,
            days_left
        )

        self._add_note(note)

        return note

    def create_recipe(self, title: str, steps: list[str]) -> Recipe:
        title = self._validate_title(title)

        note = Recipe(
            self.next_id,
            title,
            list(steps)
        )

        self._add_note(note)

        return note

    def delete_note(self, title: str) -> None:
        note = self.find_note(title)

        if note is None:
            raise ValueError("Заметка не найдена")

        self.repository.remove_note(note)
        self.repository.save_notes(self.next_id)

    def find_note(self, title: str) -> Note | None:
        title = title.strip()

        for note in self.repository.get_all_notes():
            if note.title.casefold() == title.casefold():
                return note

        return None

    def get_all_notes(self) -> list[Note]:
        return self.repository.get_all_notes()

    def get_sorted_tasks(self) -> list[Task]:
        tasks = [
            note for note in self.get_all_notes()
            if isinstance(note, Task)
        ]

        return sorted(
            tasks,
            key=lambda task: (task.days_left, task.title.casefold())
        )
