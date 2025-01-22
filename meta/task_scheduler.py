
# tasks should be returned FIFO, so maybe a queue
# ordereddict

from collections import OrderedDict

class TaskScheduler():
    def __init__(self):
        self.tasks = OrderedDict()

    def add_task(self, timestamp: int, task_id: str):
        if task_id not in self.tasks:
            self.tasks[task_id] = timestamp
            print("added:" + task_id)
    

    def run_tasks(self, timestamp: int) -> list[str]:
        tasks_to_run = []
        for key, value in self.tasks.items():
            if value <= timestamp:
                tasks_to_run.append(key)

        for key in tasks_to_run:
            del self.tasks[key]
        return tasks_to_run

scheduler = TaskScheduler()

scheduler.add_task(5, "task1")
scheduler.add_task(10, "task2")
scheduler.add_task(5, "task3")

print(scheduler.run_tasks(6))  # ["task1", "task3"]