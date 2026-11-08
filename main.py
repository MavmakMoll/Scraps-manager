
from note_repository import NoteRepository
from note_manager import NoteManager
from console_ui import ConsoleUI


def main():
    repository = NoteRepository()
    manager = NoteManager(repository)
    ui = ConsoleUI(manager)

    ui.run()


if __name__ == "__main__":
    main()
