#!/usr/bin/python3
"""Exports all employees' TODO data to JSON"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    data = {}

    # Build dictionary
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

        data[user_id] = user_tasks

    # Save file
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
#!/usr/bin/python3
"""Exports all employees' TODO data to JSON"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    data = {}

    # Build dictionary
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

        data[user_id] = user_tasks

    # Save file
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)

