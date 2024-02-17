import click
from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

from ttracker.services import (
    DisplayTask,
    create_task,
    delete_task,
    list_tasks,
    pause_task,
    resume_task,
    start_task,
    stop_task,
)


def new(name: str, start: bool):
    create_task(name, start)
    if start:
        click.echo(f"{name} added and started.")
    else:
        click.echo(f"{name} added.")


def start(name: str):
    start_task(name)
    click.echo(f"{name} started.")


def stop(name: str):
    change, total = stop_task(name)
    click.echo(f"{name} stopped. Session: {change}. Total: {total}")


def rm(name: str):
    total = delete_task(name)
    click.echo(f"{name} removed. Total time: {total}")

def resume():
    task = resume_task()
    click.echo(f"{task.name} started.")

def pause():
    task, increase = pause_task()
    click.echo(f"{task.name} stopped. Session: {increase}. Total: {task.total_time}")

def ls():
    all_tasks = list_tasks()
    if len(all_tasks) == 0:
        click.echo(f"0 tasks")
    else:
        table = make_table(all_tasks)
        Console().print(table)


def make_table(tasks: list[DisplayTask]) -> Table:
    table = Table(box=box.SIMPLE, expand=True)
    table.add_column("Name")
    table.add_column("Active")
    table.add_column("Total time")

    for t in tasks:
        if t.active_time:
            active_text = t.active_time
        else:
            active_text = "-"
        table.add_row(
            Text(t.name, overflow="ellipsis", no_wrap=True),
            Text(active_text, overflow="ellipsis", no_wrap=True),
            Text(
                text=t.total_time,
                overflow="ellipsis",
                no_wrap=True,
            ),
        )

    return table
