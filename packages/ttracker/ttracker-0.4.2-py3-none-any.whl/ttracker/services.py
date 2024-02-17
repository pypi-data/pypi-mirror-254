from dataclasses import dataclass
import datetime
from functools import cmp_to_key
from typing import Optional

from ttracker.models import Task, calculate_active_time
from ttracker.orm import CSVAdapter, Repository


def create_task(name: str, start: bool):
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        if name in [t.name for t in r.all_tasks()]:
            raise ValueError(
                "Task already exists with that name. Please remove the existing one before adding another."
            )
        if start:
            new_task = Task(name, datetime.datetime.now())
        else:
            new_task = Task(name, None)

        r.save_task(new_task)


def start_task(name: str):
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        task = r.get_task(name)
        if not task:
            raise ValueError("Task does not exist.")

        if task.active:
            raise ValueError("Task already started.")

        new_task = task.start(datetime.datetime.now())
        r.save_task(new_task)


def stop_task(name: str) -> tuple[str, str]:
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        task = r.get_task(name)
        if not task:
            raise ValueError("Task does not exist.")

        if not task.active:
            raise ValueError("Task not started.")
        
        now = datetime.datetime.now()
        new_task, increase = task.stop_task(now)
        r.save_task(new_task)

        return seconds_to_jira_time(increase), seconds_to_jira_time(new_task.cumulative_time)


def delete_task(name: str):
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        task = r.get_task(name)
        if not task:
            raise ValueError("Task does not exist.")
        if task.active:
            raise ValueError("Task started. Stop the task before running this command.")

        r.delete_task(task)
    return seconds_to_jira_time(task.cumulative_time)

def resume_task():
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        active_tasks = [t for t in r.all_tasks() if t.active]
        if len(active_tasks) > 0:
            raise ValueError("A task has already been started. Unable to resume.")
        
        inactive_tasks = [t for t in r.all_tasks() if not t.active]
        if len(inactive_tasks) == 0:
            raise ValueError("No active task. Unable to resume a task.")
        
        most_recently_stopped_task = max(inactive_tasks, key=lambda t: t.last_modified)
        new_task = most_recently_stopped_task.start(datetime.datetime.now())
        r.save_task(new_task)

        return convert_to_display_task(new_task)
    
def pause_task():
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        active_tasks = [t for t in r.all_tasks() if t.active]
        if len(active_tasks) == 0:
            raise ValueError("No active task. Unable to pause.")
        if len(active_tasks) > 1:
            raise ValueError("More than one active task. Unable to pause.")
        active_task = active_tasks[0]
        new_task, time_increase = active_task.stop_task(datetime.datetime.now())
        r.save_task(new_task)

        return convert_to_display_task(new_task), seconds_to_jira_time(time_increase)


@dataclass
class DisplayTask:
    name: str
    active: bool
    active_time: Optional[str]
    total_time: str


def task_comparator(task1, task2):
    # Custom comparator function
    if task1.active and task2.active:
        # Both tasks are active, compare by start_active_timestamp and last_modified
        if task1.start_active_timestamp > task2.start_active_timestamp:
            return -1
        elif task1.start_active_timestamp < task2.start_active_timestamp:
            return 1
        else:
            if task1.last_modified > task2.last_modified:
                return -1
            else:
                return 1
    elif task1.active:
        # Only task1 is active, it comes first
        return -1
    elif task2.active:
        # Only task2 is active, it comes first
        return 1
    else:
        # Both tasks are inactive, compare by last_modified
        if task1.last_modified > task2.last_modified:
            return -1
        else:
            return 1


def convert_to_display_task(t: Task):
    active_time = None
    if t.active:
        active_time = seconds_to_jira_time(calculate_active_time(t, datetime.datetime.now()))

    return DisplayTask(
        name=t.name,
        active=t.active,
        active_time=active_time,
        total_time=seconds_to_jira_time(t.cumulative_time),
    )


def list_tasks():
    with Repository(CSVAdapter(".ttracker.csv")) as r:
        all_tasks = sorted(r.all_tasks(), key=cmp_to_key(task_comparator))
        return [convert_to_display_task(t) for t in all_tasks]


def seconds_to_jira_time(seconds):
    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    jira_time_format = ""
    if days > 0:
        jira_time_format += f"{int(days)}d "
    if hours > 0:
        jira_time_format += f"{int(hours)}h "
    if minutes > 0:
        jira_time_format += f"{int(minutes)}m"

    if jira_time_format == "":
        jira_time_format = "0m"
    return jira_time_format.strip()
