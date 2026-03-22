from sys import argv
from task_tracker.commands import Commands
from task_tracker.help import help_, intro_

# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# - Add, Update, and Delete tasks
# - Mark a task as in progress or done
# - List all tasks
# - List all tasks that are done
# - List all tasks that are not done
# - List all tasks that are in progress

commands = ["add", "list", "delete", "update", "mark-in-progress", "mark-done", "help"]

def main():
    if len(argv) == 1:
        print("")

    if argv[1] == "add":
        Commands.add(description=argv[2])

    if argv[1] == "list":
        if len(argv) == 3:
            if argv[2] in ["progress", "done", "todo"]:
                Commands.list(filter_status_by=argv[2])
        else:
            Commands.list()

    if argv[1] == "delete":
        Commands.delete(id=int(argv[2]))

    if argv[1] == "update":
        Commands.update_description(id=int(argv[2]), description=argv[3])

    if argv[1] == "mark-in-progress":
        Commands.update_status(id=int(argv[2]), status="progress")

    if argv[1] == "mark-done":
        Commands.update_status(id=int(argv[2]), status="done")

    if argv[1] == "help":
        print(help_)

    if argv[1] not in commands:
        print("Unknown command: use help command for more info!")