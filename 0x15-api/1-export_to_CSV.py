#!/usr/bin/python3

import requests
import sys
import csv


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
            list: A list of dictionaries containing task status and title.
    """

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(todos_url)
    response.raise_for_status()
    todos_list = response.json()

    return [
        {"completed": todo["completed"], "title": todo["title"]}
        for todo in todos_list if todo["userId"] == int(emp_id)
    ]


def export_to_csv(emp_id, emp_name, todos):

    """
        Export the employee's tasks to a CSV file.

        Args:
            emp_id (int): The employee ID.
            emp_name (str): The name of the employee.
            todos (list): A list of dictionaries containing
            task status and title.
    """

    filename = f"{emp_id}.csv"
    with open(filename, mode='w', newline='') as file:
        # writer
        w = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            w.writerow([emp_id, emp_name, todo["completed"], todo["title"]])


def main():

    """
        Main function to fetch and print employee's completed tasks
        and total tasks.
    """

    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    try:
        emp_name = get_employee_name(emp_id)
        todos = get_employee_todos(emp_id)
        export_to_csv(emp_id, emp_name, todos)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
