#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys


def gather_data(employee_id):
    """Fetch and display employee TODO list progress."""
    api_uri = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch user data
        user_response = requests.get(f"{api_uri}/users/{employee_id}")
        user_response.raise_for_status()  # Check for HTTP errors
        user_data = user_response.json()
        emp_name = user_data.get("name")

        # Fetch TODO data
        todos_response = requests.get(f"{api_uri}/todos?userId={employee_id}")
        todos_response.raise_for_status()  # Check for HTTP errors
        todos_data = todos_response.json()

        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        total_tasks_done = len(done_tasks)

        # Print results
        print(
            f"Employee {emp_name} is done with tasks("
            f"{total_tasks_done}/{total_tasks}):"
        )
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
    except ValueError as e:
        print(f"Invalid data received: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
        gather_data(emp_id)
    except ValueError:
        print("Error: employee_id should be an integer")
        sys.exit(1)
