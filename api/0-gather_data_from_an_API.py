#!/usr/bin/python3
"""Fetches and displays TODO list progress for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    ).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

