class Note:
    note_type = "note"

    def __init__(self, id: int, title: str):
        self.id = id
        self.title = title

    def to_dict(self) -> dict:
        return {
            "type": self.note_type,
            "id": self.id,
            "title": self.title
        }
    def display(self) -> None:
        print(f"ID: {self.id}")
        print(f"Заголовок: {self.title}")

class TextNote(Note):
    note_type = "text"

    def __init__(self, id: int, title: str, content: str):
        super().__init__(id, title)
        self.content = content

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["content"] = self.content
        return data
    def display(self) -> None:
        super().display()
        print(f"Содержание: {self.content}")

class Task(Note):
    note_type = "task"

    def __init__(self, id: int, title: str, content: str, days_left: int):
        super().__init__(id, title)
        self.content = content
        self.days_left = days_left

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["content"] = self.content
        data["days_left"] = self.days_left
        return data
    
    def display(self) -> None:
        super().display()
        print(f"Содержание: {self.content}")
        print(f"Осталось дней: {self.days_left}")

class Recipe(Note):
    note_type = "recipe"

    def __init__(self, id: int, title: str, steps: list[str]):
        super().__init__(id, title)
        self.steps = steps

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["steps"] = self.steps
        return data
    
    def display(self) -> None:
        super().display()
        print("Шаги:")

        for number, step in enumerate(self.steps, start=1):
            print(f"{number}. {step}")