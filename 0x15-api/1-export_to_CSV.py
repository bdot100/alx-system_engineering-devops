#!/usr/bin/python3
"""This script exports to-do list information for a
given employee ID into CSV format file."""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId)).json()
    # todo variable = grabs all todos (completed or not) for the user passed in
    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(userId)).json()
    with open("{}.csv".format(userId), 'w') as acsvfile:
        csvwriter = csv.writer(acsvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            csvwriter.writerow([userId, name.get('username'),
                                task.get('completed'), task.get('title')])
