#!/usr/bin/python3
""" Exports data in the JSON format. """

if __name__ == "__main__":
    import json
    import requests
    import sys

    # Retrieve user information
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()

    # Retrieve TODO list for all users
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    # Create a dictionary to store all tasks for each user
    todoAll = {}

    # Loop through each user
    for user in users:
        taskList = []

        # Loop through tasks and filter by user ID
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                taskList.append(taskDict)

        # Store tasks in the dictionary with user ID as the key
        todoAll[user.get('id')] = taskList

    # Write the JSON data to a file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
