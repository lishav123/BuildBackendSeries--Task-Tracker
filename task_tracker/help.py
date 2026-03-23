help_ = '''
Commands:
    add, list, delete, update, mark-in-progress, mark-done

1) Using add - will add a new task to your tracker
    Syntax: task-tracker add <task>
    Example:
    $ task-tracker add "Task 1"
    Task added successfully!

2) Using list - will list your tasks (with optional status filters)
    Syntax: task-tracker list [filter]
    Filters: done, progress, todo
    Examples:
    $ task-tracker list          # Lists all tasks
    $ task-tracker list done     # Lists only completed tasks
    $ task-tracker list progress # Lists tasks currently in progress
    $ task-tracker list todo     # Lists tasks that are yet to be started

3) Using delete - will remove a task using its ID
    Syntax: task-tracker delete <id>
    Example:
    $ task-tracker delete 1
    Task 1 deleted successfully!

4) Using update - will overwrite the text of an existing task
    Syntax: task-tracker update <id> <data>
    Example:
    $ task-tracker update 1 "Updated Task 1 description"
    Task 1 updated successfully!

5) Using mark-in-progress - will change a task's status to in-progress
    Syntax: task-tracker mark-in-progress <id>
    Example:
    $ task-tracker mark-in-progress 1
    Task 1 marked as in-progress!

6) Using mark-done - will change a task's status to done
    Syntax: task-tracker mark-done <id>
    Example:
    $ task-tracker mark-done 1
    Task 1 marked as done!
'''

intro_ = '''
task-tracker: A simple, local command-line interface (CLI) to manage your daily tasks.

Keep track of your to-dos right from your terminal without any distractions. 
You can easily add new tasks, update their descriptions, track their progress 
(todo, in-progress, done), and filter your lists to see exactly what you need to work on. 
Everything is saved securely on your local desktop.

Usage:
    task-tracker <command> [arguments]

Quick Start:
    $ task-tracker add "Read the new documentation"
    $ task-tracker list todo

Tip: 
    Run `task-tracker help` to see the full list of available commands and their exact syntax.
'''