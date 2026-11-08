from note_manager import NoteManager
from models import Note


class ConsoleUI:
    def __init__(self, manager: NoteManager):
        self.manager = manager

    def run(self) -> None:
        pass

    def show_menu(self) -> None:
        pass

    def handle_choice(self, choice: int) -> None:
        pass

    def create_note_menu(self) -> None:
        pass

    def show_notes(self) -> None:
        pass

    def show_note(self, note: Note) -> None:
        pass

    def show_error(self, message: str) -> None:
        pass