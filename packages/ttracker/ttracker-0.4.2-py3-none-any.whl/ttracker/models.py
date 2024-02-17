from dataclasses import dataclass, field, replace
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Task:
    name: str
    start_active_timestamp: Optional[datetime]
    visible: bool = field(default=True)
    cumulative_time: int = field(default=0)
    last_modified: datetime = field(default=datetime.now())

    @property
    def active(self) -> bool:
        return self.start_active_timestamp is not None

    def start(self, started_at: datetime):
        if self.start_active_timestamp:
            raise ValueError("Trying to start already started task.")
        
        return replace(
            self,
            start_active_timestamp=started_at  
        )

    def stop_task(self, stopped_at: datetime):
        if self.start_active_timestamp is None:
            raise ValueError("Trying to stop task which is not active.")
        if self.start_active_timestamp > stopped_at:
            raise ValueError("Trying to stop task at a time before it started.")
        
        time_increase = round(
            (stopped_at - self.start_active_timestamp).total_seconds()
        )

        new_total_time = self.cumulative_time + time_increase
        return replace(
            self, 
            start_active_timestamp=None,
            cumulative_time=new_total_time
        ), time_increase

    def to_row(self):
        return [
            self.name,
            self.start_active_timestamp,
            self.visible,
            self.cumulative_time,
            self.last_modified,
        ]

    @staticmethod
    def to_header():
        return [
            "name",
            "start_active_timestamp",
            "visible",
            "cumulative_time",
            "last_modified",
        ]

def calculate_active_time(t: Task, now: datetime):
    if not t.start_active_timestamp:
        raise ValueError("Task not started.")
    return round((now - t.start_active_timestamp).total_seconds())