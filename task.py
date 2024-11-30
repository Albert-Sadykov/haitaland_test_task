import json
from datetime import datetime

class Task:
    def __init__(self, task_id: int, title: str, description: str, category: str,
                 due_date: str, priority: str, completed: bool = False):
        """
        Конструктор задачи.
        :param task_id: Уникальный идентификатор задачи.
        :param title: Название задачи.
        :param description: Описание задачи.
        :param category: Категория задачи (работа, личное, и т.д.).
        :param due_date: Срок выполнения задачи (строка в формате "yyyy-mm-dd").
        :param priority: Приоритет задачи (низкий, средний, высокий).
        :param completed: Статус выполнения задачи (по умолчанию False).
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')  # Преобразуем строку в дату
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        """Отметить задачу как выполненную."""
        self.completed = True

    def to_dict(self) -> dict:
        """Превратить задачу в словарь для сохранения в JSON."""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'priority': self.priority,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создать задачу из словаря (для загрузки из JSON)."""
        return cls(
            task_id=data['task_id'],
            title=data['title'],
            description=data['description'],
            category=data['category'],
            due_date=data['due_date'],
            priority=data['priority'],
            completed=data['completed']
        )

    def __str__(self):
        return f"Задача[{self.task_id}]: {self.title}, {self.priority} приоритет, описание {self.description}, дедлайн: {self.due_date}, статус: {self.completed}"

