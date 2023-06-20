class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.status = "Pending"

    def __str__(self):
        return f"{self.description} - Priority: {self.priority} - Status: {self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority):
        task = Task(description, priority)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index.")

    def view_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")
        print()
        for task1 in self.tasks:
            print(task1)

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.status = "Completed"
            print(f"Task '{task.description}' marked as completed.")
        else:
            print("Invalid task index.")

