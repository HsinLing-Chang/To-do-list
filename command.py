import argparse
import task_manager

parser = argparse.ArgumentParser()
sub_parser = parser.add_subparsers(dest="command")

# add new task parser
parser_add = sub_parser.add_parser("add", help="Add new task")
parser_add.add_argument("task", help="Add a new task with string")

# delete task parser
parser_delete = sub_parser.add_parser("delete", help="Delete task")
parser_delete.add_argument(
    "delete", type=int, help="Delete task with povided id")

# list task parser
parser_list = sub_parser.add_parser("list", help="List all tasks")
parser_list.add_argument("status", nargs="?", type=str.lower, choices=[
                         "todo", "in-progress", "done"], default=[], help="Enter one of the following status: todo, in-progress, done ")

# update parser
parser_update = sub_parser.add_parser(
    "update", help="Update the task with given id, description and status")
parser_update.add_argument("update", type=int, help="find the task with id")
parser_update.add_argument("-description", type=str, default=None,
                           help="update the description of the task")
parser_update.add_argument("-mark", type=str.lower, default=None,
                           choices=["todo", "in-progress", "done"], help="update the status of the task")

args = parser.parse_args()


# add tasks
if args.command == "add" and args.task is not None:
    task_manager.add_new_tasks(args.task)
# list tasks
if args.command == "list" and args.status:
    if args.status == "todo":
        task_manager.list_todo()
    elif args.status == "in-progress":
        task_manager.list_in_progress()
    elif args.status == "done":
        task_manager.list_done()
elif args.command == "list" and args.status == []:
    task_manager.list_all()

# update the task
if args.command == "update" and not (args.description or args.mark):
    parser.error(
        "At least one of update_description or update_status must be provided.")
elif args.command == "update" and args.update:
    task_manager.update_task(
        args.update, description=args.description, status=args.mark)

# handling deleting tasks
if args.command == "delete" and args.delete is not None:
    task_manager.delete_task(args.delete)
