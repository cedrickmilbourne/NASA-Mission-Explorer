"""
NASA Missions Explorer

Author: Cedrick D. Milbourne

Explore NASA missions using Python.
"""

from missions import MISSIONS
from nasa_api import get_apod, search_nasa_library
import textwrap
import webbrowser

def main():
    """Run the NASA Missions Explorer."""

    while True:

        print("=" * 40)
        print("      NASA Missions Explorer")
        print("=" * 40)
        print()
        print("1. View Featured Missions")
        print("2. Search Featured Missions")
        print("3. Filter Featured Missions by Destination")
        print("4. Search Featured Missions by Launch Year")
        print("5. View Featured Missions Statistics")
        print("6. NASA Astronomy Picture of the Day")
        print("7. Search NASA Image Library")
        print("8. Exit")



        choice = input("Choose an option (1-8): ")

        if choice == "1":
            show_featured_missions()
           
        elif choice == "2":
            search_featured_missions()

        elif choice == "3":
            filter_featured_missions_by_destination()

        elif choice == "4":
            search_featured_missions_by_launch_year()

        elif choice == "5":
            show_featured_mission_statistics()

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
            query = input("\nEnter a mission name to search: ")

            results = search_nasa_library(query)

            items = results["collection"]["items"]
            top_results = items[:5]

            if not items:

                print("\nNo results found.")

                input("\nPress Enter to continue...")

                continue

            print(f"\nTop {min(5, len(items))} Results")

            print("=" * 40)

            for index, item in enumerate(top_results, start=1):
                
                data = item["data"][0]

                print(f"{index}. {data.get('title', 'Unknown')}")
                

            result_choice = input(
                "\nSelect a result (1-5) or press Enter to return: "
        )

            if result_choice == "":
                continue

            if not result_choice.isdigit():
                print("\nPlease enter a number.")
                input("\nPress Enter to continue...")
                continue

            result_choice = int(result_choice)

            if result_choice < 1 or result_choice > len(top_results):
                print("\nInvalid selection.")
                input("\nPress Enter to continue...")
                continue

            selected = top_results[result_choice - 1]
            data = selected["data"][0]

            print("\nSelected NASA Library Result")
            print("=" * 40)
            print(f"Title: {data.get('title', 'Unknown')}")
            print(f"Date : {data.get('date_created', 'Unknown')[:10]}")
            print()

            if "description" in data:
                print(textwrap.fill(data["description"], width=70))
            else:
                print("Description unavailable.")

            if "links" in selected and selected["links"]:

                image_url = selected["links"][0]["href"]

                print()
                print(f"Image URL: {image_url}")
                print("=" * 40)

                open_image = input(
                    "\nWould you like to open this image in your web browser? (y/n): "
                ).lower()

                if open_image in ("y", "yes"):

                    webbrowser.open(image_url)

                    print("\nOpening image in your browser...")

            else: 
                print("\nNo image available for this result.")

            input("\nPress Enter to continue...")

        elif choice == "8":
            print("\nThank you for using NASA Missions Explorer.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")

def display_mission_details(mission):
    """Display detailed information for one mission."""

    print("\n" + "=" * 40)
    print(mission["name"])
    print("=" * 40)
    print(f"{'Launch Year' : <16}: {mission['launch_year']}")
    print(f"{'Program' : <16}: {mission['program']}")
    print(f"{'Spacecraft' : <16}: {mission['spacecraft']}")
    print(f"{'Agency' : <16}: {mission['agency']}")
    print(f"{'Launch Vehicle' : <16}: {mission['launch_vehicle']}")
    print(f"{'Launch Site' : <16}: {mission['launch_site']}")
    print(f"{'Mission Type' : <16}: {mission['mission_type']}")
    print(f"{'Destination' : <16}: {mission['destination']}")
    print(f"{'Purpose' : <16}: {mission['purpose']}")
    print(f"{'Status' : <16}: {mission['status']}")
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

def search_featured_missions():
    """Search the available NASA missions."""

    search_term = input("\nEnter the name of a featured mission (or keyword): ").lower()

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


def filter_featured_missions_by_destination():
    """Filter missions by destination."""

    destination = input("\nEnter a destination to search featured missions: ").lower()

    print("\nMatching Missions")
    print("-----------------")

    found = False

    for mission in MISSIONS.values():
        if destination in mission["destination"].lower():
            print(f"{mission['name']} ({mission['launch_year']})")
            found = True

    if not found:
        print("No missions found for that destination.")

    print()
    input("Press Enter to return to the main menu...")

def search_featured_missions_by_launch_year():
    """Search missions by launch year."""

    year = input("\nEnter a launch year for featured missions: ")

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

def show_featured_mission_statistics():
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