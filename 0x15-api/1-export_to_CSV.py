#!/usr/bin/python3
"""Using this REST API, export data in the CSV format"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Request user information
    user_id = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

    # Request the entire TODO list for all users
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    # CSV File Handling
    filename = f"{user_id}.csv"
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(user_id):
                writer.writerow([user_id, name, str(task.get('completed')),
                                 task.get('title')])
