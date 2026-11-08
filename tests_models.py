from models import TextNote, Task, Recipe

notes = [
    TextNote(1, "Покупки", "Купить молоко"),
    Task(2, "Учёба", "Изучить Python", 3),
    Recipe(3, "Завтрак", ["Нарезать овощи", "Пожарить яйца"])
]

for note in notes:
    print(note.to_dict())