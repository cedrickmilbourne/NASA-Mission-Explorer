# 🚀 NASA Missions Explorer

A modular Python command-line application for exploring historic and modern space missions using curated mission data and NASA's public APIs.

---

## Features

- Browse a curated collection of 28 historic NASA and international space missions
- Search missions by name or keyword
- Filter missions by destination
- Filter missions by launch vehicle
- View detailed mission information
- Search NASA's Images and Video Library
- Retrieve NASA's Astronomy Picture of the Day (APOD)
- Open selected NASA media directly in your web browser
- Robust input validation and user-friendly menus

---

## Technologies Used

- Python 3
- Requests
- python-dotenv
- NASA Images and Video Library API
- NASA Astronomy Picture of the Day (APOD) API

---

## Project Structure

```text
NASA_Missions_Explorer/
│
├── main.py
├── missions.py
├── nasa_api.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env (local only)
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/cedrickmilbourne/NASA_Missions_Explorer.git
```

Move into the project directory:

```bash
cd NASA_Missions_Explorer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project directory containing your NASA API key:

```text
NASA_API_KEY=your_api_key_here
```

---

## Running the Program

```bash
python main.py
```

---

## Skills Demonstrated

- Modular software design
- Python programming
- Dictionaries and lists
- REST API integration
- JSON parsing
- Environment variable management
- User input validation
- Error handling
- Browser automation
- Command-line application development

---

## Future Improvements

- Expand the mission database
- Additional filtering and sorting options
- Mission comparison tools
- Launch timeline visualization
- Export search results
- Enhanced image searching
- Graphical user interface (GUI)

---

## Why I Built This

I developed NASA Missions Explorer while completing my Bachelor of Science in Physics to strengthen my software development skills and build a technical portfolio. This project combines my interest in space exploration with practical experience in Python programming, API integration, modular software design, and command-line application development.

---

## Author

**Cedrick D. Milbourne**

Bachelor of Science in Physics (In Progress)

ARRT Registered Technologist — Radiography & Computed Tomography

---

## License

This project is intended for educational and portfolio purposes.