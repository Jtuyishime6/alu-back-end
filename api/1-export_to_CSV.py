#!/usr/bin/python3
"""Exports TODO data for a given user to CSV"""

import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

