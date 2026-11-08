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


class TextNote(Note):
    note_type = "text"

    def __init__(self, id: int, title: str, content: str):
        super().__init__(id, title)
        self.content = content

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["content"] = self.content
        return data


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


class Recipe(Note):
    note_type = "recipe"

    def __init__(self, id: int, title: str, steps: list[str]):
        super().__init__(id, title)
        self.steps = steps

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["steps"] = self.steps
        return data