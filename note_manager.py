from note_repository import NoteRepository
from models import Note, TextNote, Task, Recipe

class NoteManager():
    def __init__(self, repository: NoteRepository):
        self.repository = repository
        self.next_id: int = 1

    def find_by_id(self, note_id: int) -> Note | None:
        pass

    def find_by_title(self, title: str) -> Note | None:
        pass

    def delete_by_id(self, note_id: int) -> bool:
        pass

    def delete_by_title(self, title: str) -> bool:
        pass

    def get_all_notes(self) -> list[Note]:
        pass

    def get_sorted_tasks(self) -> list[Task]:
        pass

    def create_text_note(self, title: str, content: str) -> TextNote:
        pass

    def create_task(self, title: str, content: str, days_left: int) -> Task:
        pass

    def create_recipe(self, title: str, steps: list[str]) -> Recipe:
        pass