#!/usr/bin/python3
"""Exports TODO data for a given user to JSON"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json()
    username = user.get("username")

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    ).json()

    data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    filename = "{}.json".format(employee_id)

    with open(filename, "w") as f:
        json.dump(data, f)

