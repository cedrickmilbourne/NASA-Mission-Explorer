import os

import requests
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")


def get_apod(date=None):
    """Fetch NASA's Astronomy Picture of the Day."""

    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": NASA_API_KEY
}

    if date:
        params["date"] = date

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError:
        return None

    except requests.exceptions.RequestException:
        return None

def search_nasa_library(query):
    """Search NASA's Image and Video Library."""

    url = "https://images-api.nasa.gov/search"

    params = {
        "q": query,
        "media_type": "image"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    return response.json()