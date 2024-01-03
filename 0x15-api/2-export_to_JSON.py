#!/usr/bin/python3
""" export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests
    import sys

    # Extracting user ID from command-line argument
    userId = sys.argv[1]

    # Retrieve user information
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    
    # Retrieve TODO list for all users
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    # Create a dictionary to store user's tasks
    todoUser = {}
    taskList = []

    # Loop through tasks and filter by user ID
    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.json().get('username')
            }
            taskList.append(taskDict)

    todoUser[userId] = taskList

    # Write the JSON data to a file
    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todoUser, f)

