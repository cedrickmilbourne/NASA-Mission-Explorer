import requests


def get_apod():
    """Fetch NASA's Astronomy Picture of the Day."""

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": "DEMO_KEY"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()