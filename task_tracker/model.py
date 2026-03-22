# Task Properties
#
# Each task should have the following properties:
# - id: A unique identifier for the task
# - description: A short description of the task
# - status: The status of the task (todo, in-progress, done)
# - createdAt: The date and time when the task was created
# - updatedAt: The date and time when the task was last updated

from datetime import datetime

class TodoItem:
    def __new__(cls, id: int, description: str, status: str, created_at: str = str(datetime.now()), updated_at: str = str(datetime.now())):
        return {
            "id": id,
            "description" : description,
            "status" : status,
            "created_at" : created_at,
            "updated_at" : updated_at
        }
