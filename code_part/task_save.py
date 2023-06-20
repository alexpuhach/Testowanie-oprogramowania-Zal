from task_manager import Task

class TaskFileManager:
    @staticmethod
    def save_tasks(file_path, tasks):
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(f"{task.description},{task.priority}\n")
        print("Tasks saved successfully.")

    @staticmethod
    def load_tasks(file_path):
        tasks = []
        with open(file_path, "r") as file:
            for line in file:
                description, priority = line.strip().split(",")
                task = Task(description, priority)
                tasks.append(task)
        return tasks
