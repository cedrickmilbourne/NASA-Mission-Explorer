import requests


def get_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day."""

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "DEMO_KEY"
    }

    if date:
        params["date"] = date

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()