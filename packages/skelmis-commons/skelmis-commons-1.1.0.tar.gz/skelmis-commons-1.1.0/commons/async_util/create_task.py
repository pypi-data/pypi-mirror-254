import asyncio
import logging
from typing import Any

log = logging.getLogger(__name__)
background_tasks: set[tuple[Any, asyncio.Task]] = set()


def create_task(*args, task_id, **kwargs) -> asyncio.Task:
    """Creates a task while maintain a background reference, so they don't get de-reffed

    Parameters
    ----------
    task_id
        A unique variable to store tasks under
    """
    task = asyncio.create_task(*args, **kwargs)
    background_tasks.add((task_id, task))
    task.add_done_callback(lambda _: background_tasks.discard((task_id, task)))
    return task
