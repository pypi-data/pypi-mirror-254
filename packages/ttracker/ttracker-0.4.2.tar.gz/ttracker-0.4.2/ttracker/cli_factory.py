from dataclasses import dataclass
import click
from typing import Callable

from ttracker.commands import ls, new, pause, resume, rm, start, stop


@dataclass
class Command:
    name: str
    func: Callable
    params: list[click.Parameter]


def command_factory() -> click.Group:
    group = click.Group()

    commands = [
        Command(
            "add",
            new,
            [click.Argument(["name"]), click.Option(["--start"], is_flag=True)],
        ),
        Command(
            "start",
            start,
            [click.Argument(["name"])],
        ),
        Command(
            "stop",
            stop,
            [click.Argument(["name"])],
        ),
        Command("resume", resume, []),
        Command("pause", pause, []),
        Command("rm", rm, [click.Argument(["name"])]),
        Command("ls", ls, []),
    ]

    for c in commands:
        group.add_command(
            click.Command(
                name=c.name,
                callback=c.func,
                params=c.params,
                help=c.func.__doc__,
            )
        )

    return group
