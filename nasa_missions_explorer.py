"""
NASA Missions Explorer

Author: Cedrick D. Milbourne

Explore NASA missions using Python.
"""

from missions import MISSIONS
from nasa_api import get_apod
import textwrap
import webbrowser

def main():
    """Run the NASA Missions Explorer."""

    while True:

        print("=" * 40)
        print("      NASA Missions Explorer")
        print("=" * 40)
        print()
        print("1. View featured missions")
        print("2. Search missions")
        print("3. Filter by destination")
        print("4. Search by launch year")
        print("5. View mission statistics")
        print("6. NASA Astronomy Picture of the Day")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            show_featured_missions()
           
        elif choice == "2":
            search_missions()

        elif choice == "3":
            filter_by_destination()

        elif choice == "4":
            search_by_launch_year()

        elif choice == "5":
            show_statistics()  

        elif choice == "6":

            date = input(
                 "\nEnter a date (YYYY-MM-DD) or press Enter for today's picture: "
    )

            if date == "":
                apod = get_apod()
            else:
                apod = get_apod(date)

            print("\nNASA Astronomy Picture of the Day")
            print("=" * 40)
            print(f"Title: {apod['title']}")
            print(f"Date: {apod['date']}")
            print()
            print(textwrap.fill(apod["explanation"], width=70))
            print()
            print(f"Image URL: {apod['url']}")
            print("=" * 40)

            open_image = input(
                "\nWould you like to open this image in your web browser? (y/n): "
                ).lower()

            if open_image in ("y", "yes"):
                webbrowser.open(apod["url"])
                print("\nOpening image in your browser...")

            input("\nPress Enter to return to the main menu...")

        elif choice == "7":
            print("\nThank you for using NASA Missions Explorer.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

def display_mission_details(mission):
    """Display detailed information for one mission."""

    print("\n" + "=" * 40)
    print(mission["name"])
    print("=" * 40)
    print(f"Launch Year : {mission['launch_year']}")
    print(f"Status      : {mission['status']}")
    print(f"Mission Type: {mission['mission_type']}")
    print(f"Destination : {mission['destination']}")
    print(f"Purpose     : {mission['purpose']}")
    print("=" * 40)
    print()


def show_featured_missions():
    """Display featured NASA missions and allow the user to select one."""

    
    print("\nFeatured NASA Missions")
    print("----------------------")

    for number, mission in MISSIONS.items():
        print(f"{number}. {mission['name']}")

    print()

    choice = input("Select a mission (1-5) or press Enter to return: ")

    if choice == "":
        return

    if not choice.isdigit():
        print("\nPlease enter a number.\n")
        return

    choice = int(choice)

    if choice not in MISSIONS:
        print("\nMission not found.\n")
        return
    mission = MISSIONS[choice]
    display_mission_details(mission)
    input("Press Enter to return to the featured missions menu...")

def search_missions():
    """Search the available NASA missions."""

    search_term = input("\nEnter a mission name: ").lower()

    print("\nSearch Results")
    print("--------------")

    found = False

    for mission in MISSIONS.values():

        if (
            search_term in mission["name"].lower()
            or search_term in mission["destination"].lower()
            or search_term in mission["purpose"].lower()
            or search_term in mission["status"].lower()
            or search_term in mission["mission_type"].lower()
        ):
            display_mission_details(mission)
            found = True

    if not found:
        print("No matching missions found.")

    print()

    input("Press Enter to return to the main menu...")


def filter_by_destination():
    """Filter missions by destination."""

    destination = input("\nEnter a destination: ").lower()

    print("\nMatching Missions")
    print("-----------------")

    found = False

    for mission in MISSIONS.values():
        if destination in mission["destination"].lower():
            print(f"{mission['name']} ({mission['year']})")
            found = True

    if not found:
        print("No missions found for that destination.")

    print()
    input("Press Enter to return to the main menu...")

def search_by_launch_year():
    """Search missions by launch year."""

    year = input("\nEnter a launch year: ")

    if not year.isdigit():
        print("\nPlease enter a valid year.\n")
        return

    year = int(year)

    print("\nMissions Launched in", year)
    print("---------------------------")

    found = False

    for mission in MISSIONS.values():
        if mission["launch_year"] == year:
            print(f"{mission['name']} ({mission['destination']})")
            found = True

    if not found:
        print("No missions found for that launch year.")

    print()
    input("Press Enter to return to the main menu...")

def show_statistics():
    """Display basic statistics about the mission catalog."""

    total_missions = len(MISSIONS)

    active_count = 0
    completed_count = 0

    destinations = {}

    for mission in MISSIONS.values():
        if mission["status"] == "Active":
            active_count += 1
        elif mission["status"] == "Completed":
            completed_count += 1

        destination = mission["destination"]

        if destination in destinations:
            destinations[destination] += 1
        else:
            destinations[destination] = 1

    print("\nMission Statistics")
    print("------------------")
    print(f"Total missions   : {total_missions}")
    print(f"Active missions  : {active_count}")
    print(f"Completed missions: {completed_count}")
    print()

    print("Missions by Destination")
    print("-----------------------")

    for destination, count in destinations.items():
        print(f"{destination}: {count}")

    print()
    input("Press Enter to return to the main menu...")


if __name__ == "__main__":
    main()