#!/usr/bin/python3
"""0th task file"""

import requests
from sys import argv

if __name__ == "__main__":
    empID = argv[1]
    employeeData = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{empID}')
    employeeTODOs = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{empID}/todos').json()
    employeeName = employeeData.json()["name"]
    completedTasks = []
    countCompletedTasks = 0
    totalTasks = len(employeeTODOs)
    for todo in employeeTODOs:
        if todo["completed"] is True:
            countCompletedTasks += 1
            completedTasks.append(todo["title"])
    print("Employee {} is done with tasks({}/{}):".format(
        employeeName, countCompletedTasks, totalTasks))
    for task in completedTasks:
        print("\t{}".format(task))
