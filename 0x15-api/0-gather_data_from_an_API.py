#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    # Define URL for the REST API.
    restapi_url = "https://jsonplaceholder.typicode.com/"

    # GET request to retrieve user info
    user_info = requests.get(f"{restapi_url}users/{sys.argv[1]}").json()

    # GET request to retrieve the TODO list
    todos = requests.get(
        f"{restapi_url}todos",
        params={"userId": sys.argv[1]}
    ).json()

    # Filter completed TODO list and store titles in a list
    completed = [t.get("title") for t in todos if t.get("completed")]

    # Print employee's name, completed tasks & total no of tasks.
    print(f"Employee {user_info.get('name')} is done with tasks({len(completed)}/{len(todos)}):")

    # Print the titles of completed tasks
    [print(f"\t{c}") for c in completed]
