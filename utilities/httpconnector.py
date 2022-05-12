import requests


def get(url, headers=None, payload=None):
    response = requests.get(url=url, headers=headers)
    return response


def post(url, payload=None, headers=None):
    response = requests.post(url=url, data=payload, headers=headers)
    return response


def delete(url, payload=None, headers=None):
    response = requests.delete(url=url, data=payload, headers=headers)
    return response


def put(url, payload=None, headers=None):
    response = requests.put(url=url, data=payload, headers=headers)
    return response

