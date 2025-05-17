import unittest
from todo import Task, TaskPool
from io import StringIO
import sys

class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("Write tests")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)
        self.assertEqual(self.pool.tasks[0].title, "Write tests")

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertTrue(all(task.status == "Done" for task in done_tasks))

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
    buffer = StringIO()
    runner = unittest.TextTestRunner(stream=buffer, verbosity=2)
    result = runner.run(suite)
    output = buffer.getvalue().splitlines()

    for line in output:
        if "ok" in line and line.strip().startswith("test"):
            print(line.strip())
