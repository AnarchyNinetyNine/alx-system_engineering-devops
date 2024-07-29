#!/usr/bin/python3

"""
    Fetch and display an employee's completed tasks
    and total tasks using a public API.
"""

import requests
import sys


def get_employee_name(emp_id):

    """
        Fetch the employee name by ID from the API.
        Args:
            emp_id (int): The employee ID.
        Returns:
            str: The name of the employee.
    """

    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    response = requests.get(emp_url)
    response.raise_for_status()
    return response.json()['name']


def get_employee_todos(emp_id):

    """
        Fetch the todos for a given employee ID from the API.
        Args:
            emp_id (int): The employee ID.
        Returns:
            list: A list of completed task titles.
            int: The total number of tasks.
    """

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url)
    response.raise_for_status()
    todos_list = response.json()
    total_tasks = 0
    completed_tasks = []

    for todo in todos_list:
        if todo['userId'] == int(emp_id):
            total_tasks += 1
            if todo['completed']:
                completed_tasks.append(todo['title'])

    return completed_tasks, total_tasks


def main():

    """
        Main function to fetch and print employee's completed tasks
        and total tasks.
    """

    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    try:
        emp_name = get_employee_name(emp_id)
        completed_tasks, total_tasks = get_employee_todos(emp_id)
        count = len(completed_tasks)
        s = f"Employee {emp_name} is done with tasks({count}/{total_tasks}):"
        print(s)
        for task in completed_tasks:
            print(f"\t {task}")
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
