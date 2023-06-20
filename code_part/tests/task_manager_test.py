from unittest import TestCase
from unittest.mock import patch
from task_manager import TaskManager

class TaskManagerTest(TestCase):
    # Testowanie funkcji 'TaskManager.add_task()'
    def test_add_task(self):
        task_manager = TaskManager()
        # Dodawanie zadania
        task_manager.add_task("Complete assignment", "High")
        # Testowanie
        self.assertEqual(len(task_manager.tasks), 1)

    # Testowanie funkcji 'TaskManager.remove_task()'
    def test_remove_task(self):
        task_manager = TaskManager()
        # Dodawanie zadania
        task_manager.add_task("Complete assignment", "High")
        # Usuwanie zadania
        task_manager.remove_task(0)

        # Testowanie #1
        self.assertEqual(len(task_manager.tasks), 0)

        # Testowanie #2
        with patch('builtins.print') as mocked_print:
            task_manager.remove_task(0)
            mocked_print.assert_called_with("Invalid task index.")

    # Testowanie funkcji 'TaskManager.complete_task()'
    def test_complete_task(self):
        task_manager = TaskManager()
        # Dodawanie zadań
        task_manager.add_task("Complete assignment", "High")
        task_manager.add_task("Buy groceries", "Medium")
        task_manager.add_task("Do laundry", "Low")

        # Testowanie
        with patch('builtins.print') as mocked_print:
            task_manager.complete_task(1)
            mocked_print.assert_called_with("Task 'Buy groceries' marked as completed.")

            task_manager.complete_task(5)
            mocked_print.assert_called_with("Invalid task index.")
    
    # Testowanie funkcji 'TaskManager.view_tasks()'
    def test_view_tasks(self):
        task_manager = TaskManager()
        task_manager.add_task("Complete assignment", "High")
        task_manager.add_task("Buy groceries", "Medium")
        task_manager.add_task("Do laundry", "Low")

        with patch('builtins.print') as mocked_print:
            task_manager.view_tasks()
            mocked_print.assert_any_call("1. Complete assignment - Priority: High - Status: Pending")
            mocked_print.assert_any_call("2. Buy groceries - Priority: Medium - Status: Pending")
            mocked_print.assert_any_call("3. Do laundry - Priority: Low - Status: Pending")
            
    # Testowanie listy zadań po dodaniu do niej czegoś
    def test_task_list(self):
        task_manager = TaskManager()
        # Dodawanie zadań
        task_manager.add_task("Complete assignment", "High")
        task_manager.add_task("Buy groceries", "Medium")
        task_manager.add_task("Do laundry", "Low")
        
       
        # Tworzenie listy zadań z 'Task_manager.tasks'
        task_descriptions = [ 
            (task.description, task.priority, task.status)
            for task in task_manager.tasks
        ]

        # Tworzenie listy oczekiwanych zadań
        expected_tasks = [
            ("Complete assignment", "High", "Pending"),
            ("Buy groceries", "Medium", "Pending"),
            ("Do laundry", "Low", "Pending")
        ]

        # Testowanie
        self.assertListEqual(task_descriptions, expected_tasks)


    
