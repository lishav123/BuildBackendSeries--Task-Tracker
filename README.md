# Task Tracker CLI

## Project Link: https://roadmap.sh/projects/task-tracker

A simple, local command-line interface (CLI) application to manage your daily tasks right from your terminal. Keep track of your to-dos, update their progress, and filter your lists without any distractions.

Everything is saved securely in a local JSON file (tracker-app.json). This project was built as part of the roadmap.sh backend developer track.

## ✨ Features

- Add new tasks to your list.
- Update the description of existing tasks.
- Delete tasks you no longer need.
- Track Status by marking tasks as todo, progress, or done.
- Filter & List your tasks cleanly in a formatted table (powered by tabulate).

## 🛠️ Prerequisites

- Python 3.12 or higher
- uv (An extremely fast Python package and project manager)

## 🚀 Installation

This project is packaged using a modern `pyproject.toml` configuration. Since you are using , you can easily install it locally as an isolated, system-wide command-line tool.

- Clone this repository or download the source code.
- Navigate to the root directory of the project (where pyproject.toml is located).
- Run the following command to install the tool globally using :
```
uv tool install .
```
(Note: If you are setting this up for local development inside a virtual environment instead, you can use ```uv pip install -e .```)

This will automatically install the tabulate dependency and register the task-tracker command globally on your system.

## 💻 Usage

Once installed, you can use the task-tracker command from anywhere in your terminal.

1. Add a Task

Adds a new task to your tracker. By default, the status is set to todo.
```bash
task-tracker add "Read the new documentation"
```
2. List Tasks

Lists your tasks. You can optionally filter them by status (todo, progress, done).
```
task-tracker list          # Lists all tasks
task-tracker list done     # Lists only completed tasks
task-tracker list progress # Lists tasks currently in progress
task-tracker list todo     # Lists tasks that are yet to be started
```

3. Update a Task

Overwrites the text of an existing task using its unique ID.
```bash
task-tracker update 1 "Read the updated documentation"
```

4. Change Task Status

Update the progress of a specific task using its unique ID.

```bash
task-tracker mark-in-progress 1
task-tracker mark-done 1
```


5. Delete a Task

Removes a task from your tracker permanently using its unique ID.
```bash
task-tracker delete 1
```

6. Help Menu

If you ever forget a command or need a syntax refresher, just use the help command!

```
task-tracker help
```

## 📂 Project Structure

`main.py`: The entry point that parses terminal arguments (sys.argv) and routes them to the correct commands.

`commands.py`: Contains the core logic for adding, updating, deleting, and listing tasks.

`model.py`: Defines the TodoItem dictionary structure and auto-generates timestamps.

`tools.py`: Contains the custom `@file_tool` decorator that seamlessly handles reading and writing to the tracker-app.json file.

`help.py`: Stores the documentation and help menus.

## 👨‍💻 Author

**Lishav Tiwari (Aishwaray)**
