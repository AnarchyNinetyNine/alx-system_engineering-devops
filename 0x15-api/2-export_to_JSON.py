#!/usr/bin/python3

"""
    Fetch an employee's tasks from a public API and export them to a JSON file.
"""

import json
import requests
import sys


def get_employee_username(emp_id):

    """
        Fetch the employee username by ID from the API.

        Args:
            emp_id (int): The employee ID.

        Returns:
            str: The username of the employee.
    """

    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(emp_url)
    response.raise_for_status()
    return response.json()['username']


def get_employee_todos(emp_id):

    """
        Fetch the todos for a given employee ID from the API.

        Args:
            emp_id (int): The employee ID.

        Returns:
            list: A list of dictionaries containing task status and title.
    """

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url)
    response.raise_for_status()
    todos_list = response.json()

    return [
        {"task": todo["title"], "completed": todo["completed"]}
        for todo in todos_list if todo["userId"] == int(emp_id)
    ]


def export_to_json(emp_id, emp_username, todos):

    """
        Export the employee's tasks to a JSON file.

        Args:
            emp_id (int): The employee ID.
            emp_name (str): The name of the employee.
            todos (list): A list of dictionaries containing
            task status and title.
    """

    filename = f"{emp_id}.json"
    with open(filename, mode='w') as file:
        data = {
                str(emp_id): [
                    {
                        "task": todo["task"],
                        "completed": todo["completed"],
                        "username": emp_username
                    }
                    for todo in todos]
                }
        json.dump(data, file)


def main():

    """
        Main function to fetch and print employee's completed tasks
        and total tasks.
    """

    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    try:
        emp_username = get_employee_username(emp_id)
        todos = get_employee_todos(emp_id)
        export_to_json(emp_id, emp_username, todos)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
