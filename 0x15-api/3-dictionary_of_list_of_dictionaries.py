#!/usr/bin/python3
""" this script, using the JSONplaceholder API, for a given
    employee ID, returns all tasks from all employees, in JSON format """
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    names = requests.get('https://jsonplaceholder.typicode.com/users').json()
    # todo variable = grabs all todos (completed or not)
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/').json()

    id_dict = {}
    username_dict = {}

    for user in names:
        emp_id = user.get("id")
        id_dict[emp_id] = []
        username_dict[emp_id] = user.get('username')
    for task in todo:
        mydict = {}
        emp_id = task.get('userId')
        mydict["task"] = task.get('title')
        mydict["completed"] = task.get('completed')
        mydict["username"] = username_dict.get(emp_id)
        id_dict.get(emp_id).append(mydict)
    with open("todo_all_employees.json", 'w') as ajsonfile:
        json.dump(id_dict, ajsonfile)
