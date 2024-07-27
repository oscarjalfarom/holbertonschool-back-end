#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    api_uri = "https://jsonplaceholder.typicode.com/"

    user_data = requests.get(f"{api_uri}/users/{emp_id}").json()
    emp_name = user_data.get("name")

    todos_data = requests.get(f"{api_uri}/todos?userId={emp_id}").json()
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task["completed"]]
    total_tasks_done = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, total_tasks_done, total_tasks
    ))
    for task in done_tasks:
        print(f"\t {task['title']}")
