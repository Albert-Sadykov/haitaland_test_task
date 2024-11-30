from task_manager import TaskManager
from storage import Storage

def print_menu():
    """Выводит меню выбора действий."""
    print("\nМеню:")
    print("1. Добавить задачу")
    print("2. Удалить задачу")
    print("3. Изменить задачу")
    print("4. Пометить задачу как выполненную")
    print("5. Просмотр всех задач")
    print("6. Поиск задач")
    print("7. Выйти")

def main():
    storage = Storage()  # Создаем объект для работы с файлами
    task_manager = TaskManager(storage)  # Управление задачами
    
    while True:
        print_menu()  # Показываем меню пользователю
        choice = input("Выберите действие: ")

        if choice == '1':
            # Добавление задачи
            title = input("Название задачи: ")
            description = input("Описание задачи: ")
            category = input("Категория (например, работа, личное, обучение): ")
            due_date = input("Срок выполнения (yyyy-mm-dd): ")
            priority = input("Приоритет (низкий, средний, высокий): ")
            task_manager.add_task(title, description, category, due_date, priority)
        
        elif choice == '2':
            # Удаление задачи
            task_id = int(input("Введите ID задачи для удаления: "))
            task_manager.delete_task(task_id=task_id)
        
        elif choice == '3':
            # Изменение задачи
            task_id = int(input("Введите ID задачи для изменения: "))
            print("Что нужно изменить? Оставьте поле пустым для пропуска.")
            title = input("Новое название задачи: ")
            description = input("Новое описание задачи: ")
            category = input("Новая категория задачи: ")
            due_date = input("Новая дата выполнения (yyyy-mm-dd): ")
            priority = input("Новый приоритет (низкий, средний, высокий): ")
            task_manager.update_task(task_id, title, description, category, due_date, priority)
        
        elif choice == '4':
            # Пометка задачи как выполненной
            task_id = int(input("Введите ID задачи для отметки как выполненную: "))
            task_manager.mark_task_completed(task_id)
        
        elif choice == '5':
            # Просмотр всех задач
            print("Просмотр всех задач:")
            category_filter = input("Фильтровать по категории (оставьте пустым для всех): ")
            completed_filter = input("Фильтровать по статусу выполнения (введите 'выполнена' или 'не выполнена', оставьте пустым для всех): ")
            
            completed_filter = True if completed_filter == 'выполнена' else (False if completed_filter == 'не выполнена' else None)

            task_manager.list_tasks(category=category_filter, completed=completed_filter)
        
        elif choice == '6':
            # Поиск задач
            keyword = input("Введите ключевое слово для поиска: ")
            task_manager.search_tasks(keyword)
        
        elif choice == '7':
            # Выход из программы
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, выберите правильный вариант.")
          
if __name__ == '__main__':
    main()