
from note_manager import NoteManager


class ConsoleUI:
    def __init__(self, manager: NoteManager):
        self.manager = manager

    def run(self) -> None:
        while True:
            self.show_menu()

            choice = input("Выберите действие: ").strip()

            try:
                self.handle_choice(choice)

            except (ValueError, RuntimeError) as error:
                self.show_error(error)

    def show_menu(self) -> None:
        print("\n========== МЕНЕДЖЕР ЗАМЕТОК ==========")
        print("1. Создать заметку")
        print("2. Показать все заметки")
        print("3. Найти заметку по заголовку")
        print("4. Удалить заметку по заголовку")
        print("5. Показать задачи")
        print("0. Выход")
        print("======================================")

    def handle_choice(self, choice: str) -> None:
        if choice == "1":
            self.create_note()

        elif choice == "2":
            self.show_all_notes()

        elif choice == "3":
            self.find_note()

        elif choice == "4":
            self.delete_note()

        elif choice == "5":
            self.show_tasks()

        elif choice == "0":
            print("Завершение программы.")
            raise SystemExit

        else:
            raise ValueError("Такого пункта меню не существует")

    def show_result(self, result) -> None:
        if result is None:
            print("Заметка не найдена.")
            return

        if isinstance(result, list):
            if not result:
                print("Список пуст.")
                return

            for note in result:
                note.display()

        else:
            result.display()

    def show_error(self, error: Exception) -> None:
        print(f"\nОшибка: {error}")

    def create_note(self) -> None:
        print("\n========== СОЗДАНИЕ ЗАМЕТКИ ==========")
        print("1. Обычная заметка")
        print("2. Задача")
        print("3. Рецепт")

        choice = input("Выберите тип: ").strip()

        if choice not in ("1", "2", "3"):
            raise ValueError("Некорректный тип заметки")

        title = input("Заголовок: ").strip()

        if choice == "1":
            content = input("Содержание: ")

            note = self.manager.create_text_note(
                title,
                content
            )

        elif choice == "2":
            content = input("Содержание задачи: ")

            try:
                days_left = int(input("Количество дней: "))
            except ValueError:
                raise ValueError("Количество дней должно быть целым числом")

            note = self.manager.create_task(
                title,
                content,
                days_left
            )

        else:
            steps = []

            print("Введите шаги рецепта.")
            print("Пустая строка завершает ввод.")

            while True:
                step = input(f"Шаг {len(steps) + 1}: ").strip()

                if not step:
                    break

                steps.append(step)

            if not steps:
                raise ValueError("Рецепт должен содержать хотя бы один шаг")

            note = self.manager.create_recipe(
                title,
                steps
            )

        print("\nЗаметка успешно создана.")
        self.show_result(note)

    def show_all_notes(self) -> None:
        notes = self.manager.get_all_notes()
        self.show_result(notes)

    def find_note(self) -> None:
        title = input("Введите заголовок: ").strip()

        note = self.manager.find_note(title)
        self.show_result(note)

    def delete_note(self) -> None:
        title = input("Введите заголовок заметки: ").strip()

        self.manager.delete_note(title)

        print("Заметка успешно удалена.")

    def show_tasks(self) -> None:
        tasks = self.manager.get_sorted_tasks()
        self.show_result(tasks)
