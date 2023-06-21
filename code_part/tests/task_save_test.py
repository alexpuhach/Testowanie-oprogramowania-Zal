from unittest import TestCase
from unittest.mock import patch
from task_manager import TaskManager
from task_save import TaskFileManager
import os

class TaskFileManagerTest(TestCase):
    def setUp(self):
        # Inicjalizacja ścieżki do pliku testowego
        self.file_path = "test_tasks.txt"

        # Utworzenie instancji TaskManager
        self.task_manager = TaskManager()

        # Dodawanie zadań testowych do TaskManager
        self.task_manager.add_task("Complete assignment", "High")
        self.task_manager.add_task("Buy groceries", "Medium")
        self.task_manager.add_task("Do laundry", "Low")

    def tearDown(self):
        # Sprawdź, czy plik testowy istnieje, a jeśli tak, usuń go
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_tasks(self):
        # Sprawdź, czy zadanie zostało zapisane
        with patch('builtins.print') as mocked_print:
            TaskFileManager.save_tasks(self.file_path, self.task_manager.tasks)
            mocked_print.assert_called_with("Tasks saved successfully.")

        # Sprawdzenie, czy plik istnieje
        self.assertTrue(os.path.exists(self.file_path))

    def test_load_tasks(self):
        # Sprawdzenie, czy zadanie zostało zapisane
        with patch('builtins.print') as mocked_print:
            TaskFileManager.save_tasks(self.file_path, self.task_manager.tasks)
            mocked_print.assert_called_with("Tasks saved successfully.")

        # Wczytywanie zadania
        loaded_tasks = TaskFileManager.load_tasks(self.file_path)

        # Sprawdź, czy zadania zostały przesłane poprawnie
        self.assertEqual(len(loaded_tasks), len(self.task_manager.tasks))
        for loaded_task, original_task in zip(loaded_tasks, self.task_manager.tasks):
            self.assertEqual(loaded_task.description, original_task.description)
            self.assertEqual(loaded_task.priority, original_task.priority)

