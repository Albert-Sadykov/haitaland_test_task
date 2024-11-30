import json
from task import Task
from typing import List

class Storage:
    def __init__(self, filename: str = 'tasks.json'):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        """Загрузить задачи из файла."""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            return []  # Если файла нет, возвращаем пустой список

    def save_tasks(self, tasks: List[Task]):
        """Сохранить задачи в файл."""
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
