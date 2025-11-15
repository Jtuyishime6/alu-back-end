#!/usr/bin/python3
"""
Exports all employees' TODO data to JSON format.
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()

    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user_id
        ]

        all_data[str(user_id)] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)

