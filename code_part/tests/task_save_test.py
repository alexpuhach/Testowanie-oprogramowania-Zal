from unittest import TestCase
from unittest.mock import patch
from task_manager import TaskManager
from task_save import TaskFileManager
import os

class TaskFileManagerTest(TestCase):
    def setUp(self):
        # Ініціалізуємо шлях до тестового файлу
        self.file_path = "test_tasks.txt"

        # Створюємо екземпляр TaskManager
        self.task_manager = TaskManager()

        # Додаємо тестові завдання до TaskManager
        self.task_manager.add_task("Complete assignment", "High")
        self.task_manager.add_task("Buy groceries", "Medium")
        self.task_manager.add_task("Do laundry", "Low")

    def tearDown(self):
        # Перевіряємо, чи існує тестовий файл, і якщо так, видаляємо його
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_tasks(self):
        # Перевіряємо збереження завдання 
        with patch('builtins.print') as mocked_print:
            TaskFileManager.save_tasks(self.file_path, self.task_manager.tasks)
            mocked_print.assert_called_with("Tasks saved successfully.")

        # Перевіряємо, чи файл існує
        self.assertTrue(os.path.exists(self.file_path))

    def test_load_tasks(self):
        # Перевіряємо збереження завдання 
        with patch('builtins.print') as mocked_print:
            TaskFileManager.save_tasks(self.file_path, self.task_manager.tasks)
            mocked_print.assert_called_with("Tasks saved successfully.")

        # Завантажуємо завдання
        loaded_tasks = TaskFileManager.load_tasks(self.file_path)

        # Перевіряємо, чи завдання завантажені коректно
        self.assertEqual(len(loaded_tasks), len(self.task_manager.tasks))
        for loaded_task, original_task in zip(loaded_tasks, self.task_manager.tasks):
            self.assertEqual(loaded_task.description, original_task.description)
            self.assertEqual(loaded_task.priority, original_task.priority)

