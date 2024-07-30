#!/usr/bin/python3

"""
    This script exports data in the JSON format.
    It records all tasks from all employees and saves them to a file.
"""


import json
import requests


def fetch_data():

    """ Fetch & Return data """

    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    # Fetch users
    users = requests.get(users_url).json()

    # Fetch todos
    todos = requests.get(todos_url).json()

    # Prepare the data
    data = {}
    for user in users:
        user_id = str(user['id'])
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            for todo in todos if todo['userId'] == user['id']
        ]

        data[user_id] = user_tasks

    return data


def save_to_json(data):

    """ Export data to a JSON file. """

    with open('todo_all_employees.json', 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    data = fetch_data()
    save_to_json(data)
