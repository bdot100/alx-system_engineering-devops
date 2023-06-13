#!/usr/bin/python3

import requests


def validate_hostname(api_key, app_key, hostname):
    url = "https://api.datadoghq.com/api/v1/hosts"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    response = requests.get(url, headers=headers, params=hostname)

    if response.status_code == 200:
        print("Hostname is valid")
    elif response.status_code == 404:
        print("Hostname not found", response.status_code)
    else:
        print("Error occurred:", response.status_code)

# Datadog API key and application key
api_key = "74a4f021878681fb73dcd43873685bdf"
app_key = "66d3f41e93e893e9398d585dc6507783014ad906"

# The hostname you want to validate
hostname = "183995-web-01"

# Call the function to validate the hostname
validate_hostname(api_key, app_key, hostname)

