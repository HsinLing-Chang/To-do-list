import json
import os
from datetime import datetime
from tabulate import tabulate
file_path = "task.json"
headers = ["Id", "Description", "Status", "CreatAt", "UpdatedAt"]


# update and delete data displayed
def update_and_delete_table(task):
    data = [
        [
            task["id"],
            task["description"],
            task["status"],
            task["createdAt"],
            task["updatedAt"]
        ]
    ]
    table = tabulate(data, headers=headers, tablefmt="grid")
    return table
# create table on CLI


def create_tables(task_lst):
    data = []
    for task in task_lst:
        data.append(
            [task["id"],
             task["description"],
             task["status"],
             task["createdAt"],
             task["updatedAt"]]
        )
    table = tabulate(data, headers=headers, tablefmt="grid")
    return table


# chechk if the file exists
if not os.path.exists(file_path):
    data = {
        "tasks": []
    }

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

# open tasks


def open_tasks():
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []


# save tasks

def save_tasks(tasks):
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)


# add new task
def add_new_tasks(description: str):
    currentData = open_tasks()
    id = len(currentData["tasks"]) + 1
    new_task = {
        "id": id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "updatedAt": None
    }
    currentData["tasks"].append(new_task)
    save_tasks(currentData)
    # create a table
    table = update_and_delete_table(new_task)
    print(table)

# Upadate task with provided id


def update_task(id, description: str = None, status: str = None):
    currentData = open_tasks()
    task_index = id-1
    status_allowed = ["todo", "done", "in-progress"]
    try:
        tasks_dict = {
            task["id"]: task for task in currentData["tasks"] if task["id"] == id}
        task = tasks_dict.get(id)  # 用 id 查找

        if status in status_allowed or status is None:
            update_description = description if description is not None else task["description"]
            update_status = status if status is not None else task["status"]
        else:
            raise ValueError(f"Status must be one of the following : {
                             ", ".join(status_allowed)}")
        update_task = {
            "id": id,
            "description": update_description,
            "status": update_status,
            "createdAt": task["createdAt"],
            "updatedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        currentData["tasks"].pop(task_index)
        currentData["tasks"].insert(task_index, update_task)
        save_tasks(currentData)
        # create a table
        table = update_and_delete_table(update_task)
        print(table)
    except ValueError as e:
        print(e)
    except Exception:
        print("This id cannot be found. Pleas try again.")


# delete task with provided id


def delete_task(id):
    try:
        task_index = id-1
        currentData = open_tasks()
        delete_data = currentData["tasks"].pop(task_index)
        save_tasks(currentData)
        # create a table that have been deleted
        table = update_and_delete_table(delete_data)
        print(table)
    except:
        print("This id cannot be found, please try again.")


def list_all():
    currentData = open_tasks()
    if currentData["tasks"]:
        table = create_tables(currentData["tasks"])
        print(table)
    else:
        print("There are no tasks yet. Please add a new task.")


def list_done():
    currentData = open_tasks()
    task_lst = [task for task in currentData["tasks"]
                if task["status"] == "done"]
    if task_lst:
        table = create_tables(task_lst)
        print(table)
    else:
        print("Tasks cannot be found.")


def list_todo():
    currentData = open_tasks()
    task_lst = [task for task in currentData["tasks"]
                if task["status"] == "todo"]
    if task_lst:
        table = create_tables(task_lst)
        print(table)
    else:
        print("Tasks cannot be found.")


def list_in_progress():
    currentData = open_tasks()
    task_lst = [task for task in currentData["tasks"]
                if task["status"] == "in-progress"]
    if task_lst:
        table = create_tables(task_lst)
        print(table)
    else:
        print("Tasks cannot be found.")
