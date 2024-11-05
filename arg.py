import argparse
import task_manager

parser = argparse.ArgumentParser()
sub_parser = parser.add_subparsers(dest="command")
# add new task parser
parser_add = sub_parser.add_parser("add", help="add new task")
parser_add.add_argument("description", help="Add a new task with string")
# delete task parser
parser_delete = sub_parser.add_parser("delete", help="delete task")
parser_delete.add_argument(
    "delete", type=int, help="delete task with povided id")
# list all task parser
parser_list = sub_parser.add_parser("list", help="List all tasks")
parser_list.add_argument("status", nargs="?", type=str.lower, choices=[
                         "todo", "in-progress", "done"], default=[], help="Enter one of the following status: todo, in-progress, done ")

args = parser.parse_args()

# handling adding tasks
if args.command == "add" and args.description is not None:
    task_manager.add_new_tasks(args.description)
# handling listing tasks
if args.command == "list" and args.status:
    if args.status == "todo":
        task_manager.list_todo()
    elif args.status == "in-progress":
        task_manager.list_in_progress()
    elif args.status == "done":
        task_manager.list_done()
elif args.status == []:
    task_manager.list_all()
# handling deleting tasks
if args.command == "delete" and args.delete is not None:
    task_manager.delete_task(args.delete)
