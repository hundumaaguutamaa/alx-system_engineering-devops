#!/usr/bin/python3
""" Gather data from an API"""

import requests
import sys

if __name__ == "__main__":
    """Define REST API url"""
    restapi_url = "https://jsonplaceholder.typicode.com"

    # Get employee ID from command-line arguments
    employee_id = int(sys.argv[1])

    # Get employee details
    user_response = requests.get(f"{restapi_url}/users/{employee_id}")
    user_data = user_response.json()

    # Get employee's TODO list
    todo_response = requests.get(f"{restapi_url}/todos?userId={employee_id}")
    todo_data = todo_response.json()

    # Calculate progress
    total_task = len(todo_data)
    completed_task = sum(task['completed'] for task in todo_data)

    # Display progress information
    print(f"Employee {user_data['name']} is done with tasks ({completed_task}/{total_task}):")
    print(f"{user_data['name']}:{completed_task}/{total_task}")
