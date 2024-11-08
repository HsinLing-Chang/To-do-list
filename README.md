# To-do-list

Sample solution for the task-tracker challenge from roadmap.sh.

## Introduction

This project is a command-line interface (CLI) application that allows users to manage tasks efficiently by providing features like adding, deleting, updating, and listing tasks.

## Features

- **Add new tasks**: Users can add new tasks to task manager by providing a description. Each task will be assigned a unique ID. The initial status would be set to "todo".
- **Delete tasks**: Users can delete the task from the list by providing the task's unique ID.
- **Update tasks**: The description and status can be update. This requires the task's ID. Users can choose either update the description or status of the task, or they can update both.
- **List tasks**: Users can view all tasks in the list or filter them by status. The statuses available for filtering are "todo", "in-progress" and "done".

## Project Strcture

- **task_manager.py**:
  This is the main Python script that manages the execution of all tasks. It contains functions to :
  - **Add** new tasks to the task list.
  - **Delete** tasks by ID.
  - **Update** the description and status of tasks.
  - **List** all tasks with optional status filtering.
- **command.py**:
  This script is responsible for parsing user command from the CLI using the `argparse` module. The commands allows user to interact with to-do list.
  The `command.py` script calls the relevent function from `task_manager.py` to execute the action based on the user's input.
- **task.json**:
  The tasks are stored in a JSON file (`task.json`) for persistent data storage. If the file doesn't exist, it will create one in the current directory.

## Installation and Usage

### Installation:

To get started with this project, clone the repository to your local machine:
`   git clone https://github.com/HsinLing-Chang/To-do-list.git
  `

### Usage:

- **Add a task**

```
python command.py add "Say Hi to a stranger"
```

-**List a task**

- List all tasks
  ```
  python command.py list
  ```
- List tasks by status

  ```
  # Tasks that are marked as todo
  python command.py list todo

  # Tasks that are marked as in-progress
  python command.py list in-progress

  # Tasks that are marked as done
  python command.py list done
  ```

- **Update a task**
  By providing the task ID, users can update the description, the status, or both.

```
# Update description of the task
python command.py updata 1 "Say Hi to two stranger"

# Update status of the task
python command.py update 1 -mark done

#Update both
python command.py update 1 "Say Hi to two stranger" -mark done
```

- **Delete a task**

```
python command.py delete 1
```

## Sample JSON structure

```
{
  "tasks": [
      {
          "id": 1,
          "description": "Say Hi to a stranger",
          "status": "todo" ,
          "createdAt":  "08/11/2024 11:04:07"
          "updatedAt": null
      },

  ]
}
```
