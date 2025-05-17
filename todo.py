class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status

class TaskPool:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def populate(self):
        self.tasks = [
            Task("Write code", "ToDo"),
            Task("Fix bugs", "ToDo"),
            Task("Push to GitHub", "Done"),
        ]

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]
