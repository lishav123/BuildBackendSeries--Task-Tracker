# Task Properties
#
# Each task should have the following properties:
# - id: A unique identifier for the task
# - description: A short description of the task
# - status: The status of the task (todo, in-progress, done)
# - createdAt: The date and time when the task was created
# - updatedAt: The date and time when the task was last updated

from datetime import datetime

class Status:
    status = ["todo", "in progress", "done"]

class TodoItem:
    def __init__(self, id: int, description: str, status: Status, created_at: datetime, updated_at: datetime):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

