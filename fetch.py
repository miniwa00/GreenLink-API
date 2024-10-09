import requests

URL = "http://127.0.0.1:8000/data"


def fetch_data_by_feature(feature_name):
    url = f"{URL}/feature/{feature_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_company_data(company_name):
    url = f"{URL}/company/{company_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_company_average(company_name):
    url = f"{URL}/company/{company_name}/average"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def fetch_yearly_average():
    url = f"{URL}/yearly_average"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {}


def fetch_data_by_year(year):
    url = f"{URL}/year/{year}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_max_feature(feature_name):
    url = f"{URL}/max/{feature_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


def fetch_min_feature(feature_name):
    url = f"{URL}/min/{feature_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []
