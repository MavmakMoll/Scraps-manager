from models import TextNote, Task, Recipe
from note_repository import NoteRepository

repository = NoteRepository()

repository.add_note(TextNote(1, "Покупки", "Купить молоко"))
repository.add_note(Task(2, "Учёба", "Изучить Python", 3))
repository.add_note(Recipe(3, "Завтрак", ["Нарезать овощи", "Пожарить яйца"]))

repository.save_notes(4)