import csv
from dataclasses import replace
from datetime import datetime
import os
from pathlib import Path
from typing import Optional
from ttracker.models import Task


class CSVAdapter:
    def __init__(self, filename: str, save_path: Optional[Path] = None):
        if save_path is None:
            save_path = Path(os.path.expanduser("~"))

        self.file = save_path / filename

    def read(self) -> list[Task]:
        tasks = []
        try:
            with open(self.file, mode="r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)
                if header != Task.to_header():
                    raise ValueError("Invalid CSV format.")
                for row in reader:
                    task = Task(
                        name=row[0],
                        visible=bool(row[2]),
                        cumulative_time=int(row[3]),
                        start_active_timestamp=datetime.fromisoformat(row[1])
                        if row[1]
                        else None,
                        last_modified=datetime.fromisoformat(row[4]),
                    )
                    tasks.append(task)
        except FileNotFoundError:
            pass  # File doesn't exist, return an empty list of tasks
        return tasks

    def write(self, tasks: list[Task]) -> None:
        with open(self.file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(Task.to_header())
            writer.writerows([task.to_row() for task in tasks])


class Repository:
    def __init__(self, adapter: CSVAdapter):
        self.adapter = adapter

    def __enter__(self):
        self.tasks = self.adapter.read()
        return self

    def __exit__(self, type, value, traceback):
        self.adapter.write(self.tasks)

    def get_task(self, name: str) -> Optional[Task]:
        return next((t for t in self.tasks if t.name == name), None)

    def all_tasks(self) -> list[Task]:
        return self.tasks

    def save_task(self, task: Task) -> None:
        for i, t in enumerate(self.tasks):
            if t.name == task.name:
                self.tasks[i] = replace(task, last_modified=datetime.now())
                return
        self.tasks.append(replace(task, last_modified=datetime.now()))

    def delete_task(self, task: Task):
        self.tasks = [t for t in self.tasks if t != task]
