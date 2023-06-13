#!/usr/bin/python3

import requests
import json


def validate_hostname(api_key, app_key):
    url = "https://api.datadoghq.com/api/v1/dashboard"
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key
    }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)

    #print(data)
    for key, value in data.items():
        print(f"{key}: {value}")


# Datadog API key and application key
api_key = ""
app_key = ""

# Call the function to validate the hostname
validate_hostname(api_key, app_key)