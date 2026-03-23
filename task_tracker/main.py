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
        print(intro_)
        return

    if argv[1] == "add":
        if len(argv) > 2:
            print("Wrong use of add command! use help command for more info!")
            return

        try:
            Commands.add(description=argv[2])
        except IndexError:
            print("Wrong use of add command! use help command for more info!")
        return

    if argv[1] == "list":
        if len(argv) == 3:
            if argv[2] in ["progress", "done", "todo"]:
                Commands.list(filter_status_by=argv[2])
            else:
                print("Use [progress, done, todo] only")

        elif len(argv) == 2:
            Commands.list()
        else:
            print("Wrong use of list command! use help command for more info!")
        return

    if argv[1] == "delete":
        if len(argv) > 3:
            print("Wrong use of delete command! use help command for more info!")
        else:
            try:
                Commands.delete(id=int(argv[2]))
            except IndexError:
                print("Wrong use of delete command! use help command for more info!")
            except ValueError:
                print("Use id as an integer to delete!")
        return

    if argv[1] == "update":
        if len(argv) > 4:
            print("Wrong use of update command! use help command for more info!")
        else:
            try:
                Commands.update_description(id=int(argv[2]), description=argv[3])
            except IndexError:
                print("Wrong use of update command! use help command for more info!")
            except ValueError:
                print("Use id as an integer to update!")
        return

    if argv[1] == "mark-in-progress":
        if len(argv) > 3:
            print("Wrong use of mark-in-progress command! use help command for more info!")
        else:
            try:
                Commands.update_status(id=int(argv[2]), status="progress")
            except IndexError:
                print("Wrong use of update command! use help command for more info!")
            except ValueError:
                print("Use id as an integer to update!")
        return

    if argv[1] == "mark-done":
        if len(argv) > 3:
            print("Wrong use of mark-in-progress command! use help command for more info!")
        else:
            try:
                Commands.update_status(id=int(argv[2]), status="done")
            except IndexError:
                print("Wrong use of update command! use help command for more info!")
            except ValueError:
                print("Use id as an integer to update!")
        return

    if argv[1] == "help":
        print(help_)
        return

    if argv[1] not in commands:
        print("Unknown command: use help command for more info!")
        return