# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# - Add, Update, and Delete tasks
# - Mark a task as in progress or done
# - List all tasks
# - List all tasks that are done
# - List all tasks that are not done
# - List all tasks that are in progress

from datetime import datetime

from task_tracker.tools import file_tool
from task_tracker.model import TodoItem

from tabulate import tabulate # used only for good table structure

class Commands:

    @staticmethod
    @file_tool("tracker-app.json")
    def add(data: list | dict, description: str):
        """
        usage: task-tracker add <description>
        - Will add your task in your tracker

        example:
        $ task-tracker add "Add Item"
        Item added used `task-tracker list` to see your tasks.
        """
        if isinstance(data, list):
            print("Item added used `task-tracker list` to see your tasks.")
            if not len(data) > 0:
                data += [TodoItem(id=0, description=description, status="todo")]
            else:
                data += [TodoItem(id=data[-1]["id"] + 1, description=description, status="todo")]
            return data

        else:
            raise TypeError("Explicitly data is being changed, use list and dict with id")

    @staticmethod
    @file_tool("tracker-app.json")
    def update_description(data: dict | list, id: int, description: str):
        """
        usage: task-tracker update <id> <description>
        - Will update your task in your tracker

        example:
        $ task-tracker update 0 "New Item"
        updated the description of id `0` to `new Item` successfully.
        """
        if data is None:
            print("Nothing added anything yet to display!")

        else:
            dt = list(filter(lambda item: item["id"] == id, data))
            if len(dt) == 0:
                print("ID ain't available")
            else:
                print(f"Item updated successfully!")
                return list(
                    map(
                        lambda item: TodoItem(
                            id=item["id"],
                            description=description,
                            status=item["status"],
                            created_at=item["created_at"],
                            updated_at=str(datetime.now())
                        ) if item["id"] == id else item, data
                    )
                )

    @staticmethod
    @file_tool("tracker-app.json")
    def update_status(data: dict | list, id: int, status: str):
        if data is None:
            print("Nothing added anything yet to display!")

        else:
            dt = list(filter(lambda item: item["id"] == id, data))
            if len(dt) == 0:
                print("ID ain't available")
            else:
                print(f"status: {status} updated successfully!")
                return list(
                    map(
                        lambda item: TodoItem(
                            id=item["id"],
                            description=item["description"],
                            status=status,
                            created_at=item["created_at"],
                            updated_at=str(datetime.now())
                        ) if item["id"] == id else item, data
                    )
                )

    @staticmethod
    @file_tool("tracker-app.json")
    def delete(data: dict | list, id: int):
        """
        usage: tracker-app delete <id>
        - Will delete your task in your tracker
        """
        new_data = list(filter(lambda item: item["id"] != id, data))
        if len(new_data) == len(data):
            print("ID ain't available")
        print(f"Id: {id} successfully deleted!")
        return new_data

    @staticmethod
    @file_tool("tracker-app.json")
    def list(data: dict | list, filter_status_by: str | None = None):
        """
        usage: tracker-app list <status>
        - Will list your task in your tracker
        """
        if data is None:
            print("Nothing added anything yet to display!")

        if filter_status_by is None:
            print(tabulate(data, headers="keys", tablefmt="outline"))

        if filter_status_by in ["todo", "progress", "done"]:
            print(tabulate(list(filter(lambda item: item["status"] == filter_status_by, data)), headers="keys", tablefmt="outline"))

if __name__ == "__main__":
    Commands.add(description="Task 1")
    Commands.add(description="Task 2")
    Commands.update_description(id=3, description="Task 3")
    Commands.update_description(id=4, description="Task 4")
    Commands.update_status(id=5, status="pending")
    Commands.update_status(id=6, status="done")
    Commands.delete(id=7)
    Commands.delete(id=1)
    Commands.delete(id=5)
    Commands.list()
    print()
    Commands.list(filter_status_by="done")
