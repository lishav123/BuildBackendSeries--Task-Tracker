from sys import argv
from commands import Commands

# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# - Add, Update, and Delete tasks
# - Mark a task as in progress or done
# - List all tasks
# - List all tasks that are done
# - List all tasks that are not done
# - List all tasks that are in progress

commands = ["add", "list", "delete", "update"]

if argv[1] == "add":
    Commands.add(description=argv[2])

if argv[1] == "list":
    Commands.list()

if argv[1] == "delete":
    Commands.delete(id=int(argv[2]))

if argv[1] == "update":
    Commands.update_description(id=int(argv[2]), description=argv[3])