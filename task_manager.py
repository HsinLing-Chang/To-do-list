import json
import os
from datetime import datetime

file_path = "task.json"

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


# Upadate task with provided id

def update_task(id, description=None, status: str = None):
    currentData = open_tasks()
    try:
        tasks_dict = {
            task["id"]: task for task in currentData["tasks"] if task["id"] == id}
        task = tasks_dict.get(id)  # 用 id 查找
        update_description = description if description is not None else task["description"]
        update_status = status if status is not None else task["status"]
        update_task = {
            "id": id,
            "description": update_description,
            "status": update_status,
            "createdAt": task["createdAt"],
            "updatedAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        currentData["tasks"].pop(id-1)
        currentData["tasks"].insert(id-1, update_task)
        save_tasks(currentData)
    except Exception:
        print("請輸入正確的id與內容")

# delete task with provided id


def delete_task(id):
    try:
        currentData = open_tasks()
        currentData["tasks"].pop(id - 1)
        save_tasks(currentData)
    except:
        print("找不到此id，請重新輸入")
