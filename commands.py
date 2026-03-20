# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# - Add, Update, and Delete tasks
# - Mark a task as in progress or done
# - List all tasks
# - List all tasks that are done
# - List all tasks that are not done
# - List all tasks that are in progress

import os
import json

def file(filename: str):
    def inner():
        with open(filename) as f:
            ...

    return inner

class Commands:

    @staticmethod
    def add():
        """
        usage: tracker-app add <description>
        - Will add your task in your tracker
        """
        ...

    @staticmethod
    def update():
        """
        usage: tracker-app update <id> <description>
        - Will update your task in your tracker
        """
        ...

    @staticmethod
    def delete():
        """
        usage: tracker-app delete <id>
        - Will delete your task in your tracker
        """
        ...

    @staticmethod
    def mark():
        """
        usage: tracker-app mark <id> <status>
        - Will mark your task in your tracker
        """
        ...

    @staticmethod
    def list():
        """
        usage: tracker-app list <status>
        - Will list your task in your tracker
        """
        ...