from typing import List, Optional
from task import Task
import json

class TaskManager:
    def __init__(self, storage):
        self.storage = storage  # Объект для работы с файлами
        self.tasks = self.storage.load_tasks()  # Загружаем задачи при старте

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str):
        """Добавить новую задачу."""
        task_id = len(self.tasks) + 1  # Простой способ генерации уникального ID
        new_task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(new_task)
        self.storage.save_tasks(self.tasks)
        print(f"Задача '{title}' добавлена.")

    def delete_task(self, task_id: Optional[int] = None, category: Optional[str] = None):
        """Удалить задачу по ID или по категории."""
        if task_id is not None:
            self.tasks = [task for task in self.tasks if task.task_id != task_id]
        elif category:
            self.tasks = [task for task in self.tasks if task.category != category]
        else:
            print("Не указан параметр для удаления.")
            return
        self.storage.save_tasks(self.tasks)
        print(f"Задачи удалены.")

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                    category: Optional[str] = None, due_date: Optional[str] = None, priority: Optional[str] = None):
        """Редактировать задачу."""
        task = next((task for task in self.tasks if task.task_id == task_id), None)
        if task:
            if title: task.title = title
            if description: task.description = description
            if category: task.category = category
            if due_date: task.due_date = due_date
            if priority: task.priority = priority
            self.storage.save_tasks(self.tasks)
            print(f"Задача {task_id} обновлена.")
        else:
            print(f"Задача с ID {task_id} не найдена.")

    def mark_task_completed(self, task_id: int):
        """Отметить задачу как выполненную."""
        task = next((task for task in self.tasks if task.task_id == task_id), None)
        if task:
            task.mark_completed()
            self.storage.save_tasks(self.tasks)
            print(f"Задача {task_id} помечена как выполненная.")
        else:
            print(f"Задача с ID {task_id} не найдена.")

    def list_tasks(self, category: Optional[str] = None, completed: Optional[bool] = None):
        """Просмотр всех задач с возможностью фильтрации по категории и статусу."""
        tasks_to_show = self.tasks
        if category:
            tasks_to_show = [task for task in tasks_to_show if task.category == category]
        if completed is not None:
            tasks_to_show = [task for task in tasks_to_show if task.completed == completed]

        for task in tasks_to_show:
            print(task)

    def search_tasks(self, keyword: str):
        """Поиск задач по ключевым словам в названии или описании."""
        result = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for task in result:
            print(task)
