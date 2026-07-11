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
        print("4. Filter Featured Missions by Launch Year")
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
            filter_featured_missions_by_launch_year()

        elif choice == "5":
            show_featured_mission_statistics()

        elif choice == "6":
            browse_apod()

        elif choice == "7":
            search_nasa_media_library()

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
    
    media_choice = input(
    "\nWould you like to search NASA media for this mission? (y/n): "
    ).lower()

    if media_choice in ("y", "yes"):
        search_media_for_mission(mission)


def show_featured_missions():
    """Display featured NASA missions and allow the user to select one."""

    while True:

        print("\nFeatured NASA Missions")
        print("----------------------")

        for number, mission in MISSIONS.items():
            print(f"{number}. {mission['name']}")

        print()

        choice = input(
            "Select a mission (1-28) or press Enter to return: "
        )

        if choice == "":
            return

        if not choice.isdigit():
            print("\nPlease enter a number.\n")
            continue

        choice = int(choice)

        if choice not in MISSIONS:
            print("\nMission not found.\n")
            continue

        mission = MISSIONS[choice]

        display_mission_details(mission)
    

def search_featured_missions():
    """Search featured NASA missions using a mission name or keyword."""

    while True:
        search_term = input(
            "\nEnter a featured mission keyword "
            "or press Enter to return: "
        ).strip().lower()

        if search_term == "":
            return

        matches = []

        for mission in MISSIONS.values():
            if (
                search_term in mission["name"].lower()
                or search_term in mission["destination"].lower()
                or search_term in mission["purpose"].lower()
                or search_term in mission["status"].lower()
                or search_term in mission["mission_type"].lower()
                or search_term in mission["program"].lower()
                or search_term in mission["agency"].lower()
                or search_term in mission["spacecraft"].lower()
                or search_term in mission["launch_vehicle"].lower()
                or search_term in mission["launch_site"].lower()
            ):
                matches.append(mission)

        if not matches:
            print("\nNo matching missions found.")
            continue

        print("\nSearch Results")
        print("--------------")

        choose_mission_from_results(matches)

def filter_featured_missions_by_destination():
    """Filter featured missions by destination."""

    while True:
        destination = input(
            "\nEnter a destination "
            "or press Enter to return: "
        ).strip().lower()

        if destination == "":
            return

        matches = []

        for mission in MISSIONS.values():
            if destination in mission["destination"].lower():
                matches.append(mission)

        if not matches:
            print("\nNo featured missions found for that destination.")
            continue

        print("\nMatching Missions")
        print("-----------------")

        choose_mission_from_results(matches)

def filter_featured_missions_by_launch_year():
    """Filter featured missions by launch year."""

    while True:
        year_input = input(
            "\nEnter a launch year "
            "or press Enter to return: "
        ).strip()

        if year_input == "":
            return

        if not year_input.isdigit():
            print("\nPlease enter a valid year.")
            continue

        launch_year = int(year_input)

        matches = []

        for mission in MISSIONS.values():
            if mission["launch_year"] == launch_year:
                matches.append(mission)

        if not matches:
            print(
                f"\nNo featured missions found for {launch_year}."
            )
            continue

        print("\nMatching Missions")
        print("-----------------")

        choose_mission_from_results(matches)


def choose_mission_from_results(matches):
    """Allow the user to select and view one mission from a result list."""

    if not matches:
        return

    while True:
        print()

        for index, mission in enumerate(matches, start=1):
            print(f"{index}. {mission['name']} ({mission['launch_year']})")

        choice = input(
            f"\nSelect a mission (1-{len(matches)}) "
            "or press Enter to return: "
        ).strip()

        if choice == "":
            return

        if not choice.isdigit():
            print("\nPlease enter a number.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(matches):
            print("\nInvalid selection.")
            continue

        selected_mission = matches[choice - 1]
        display_mission_details(selected_mission)


def search_media_for_mission(mission):
    """Search the NASA Image Library for a selected featured mission."""

    query = mission["name"]

    print(f"\nSearching NASA media for {mission['name']}...")

    results = search_nasa_library(query)
    items = results["collection"]["items"]

    browse_nasa_media_results(items)


def browse_nasa_media_results(items):
    """Display NASA media results and allow repeated selections."""

    top_results = []
    seen_titles = set()

    for item in items:
        data_list = item.get("data", [])

        if not data_list:
            continue

        data = data_list[0]
        title = data.get("title", "Unknown").strip()
        normalized_title = title.lower()

        if normalized_title not in seen_titles:
            top_results.append(item)
            seen_titles.add(normalized_title)

        if len(top_results) == 10:
            break

    if not top_results:
        print("\nNo NASA media results found.")
        input("\nPress Enter to return...")
        return

    while True:
        print(f"\nTop {len(top_results)} NASA Media Results")
        print("=" * 40)

        for index, item in enumerate(top_results, start=1):
            data = item["data"][0]
            print(f"{index}. {data.get('title', 'Unknown')}")

        result_choice = input(
            f"\nSelect a result (1-{len(top_results)}) "
            "or press Enter to return: "
        ).strip()

        if result_choice == "":
            return

        if not result_choice.isdigit():
            print("\nPlease enter a valid number.")
            input("\nPress Enter to continue...")
            continue

        result_number = int(result_choice)

        if result_number < 1 or result_number > len(top_results):
            print("\nInvalid selection.")
            input("\nPress Enter to continue...")
            continue

        selected = top_results[result_number - 1]
        data = selected["data"][0]

        print("\nSelected NASA Media Result")
        print("=" * 40)
        print(f"Title: {data.get('title', 'Unknown')}")
        print(f"Date : {data.get('date_created', 'Unknown')[:10]}")
        print()

        description = data.get("description", "Description unavailable.")
        print(textwrap.fill(description, width=70))

        links = selected.get("links", [])

        if links:
            image_url = links[0].get("href")

            if image_url:
                print()
                print(f"Image URL: {image_url}")
                print("=" * 40)

                open_image = input(
                    "\nWould you like to open this image "
                    "in your web browser? (y/n): "
                ).lower()

                if open_image in ("y", "yes"):
                    webbrowser.open(image_url)
                    print("\nOpening image in your browser...")
        else:
            print("\nNo image is available for this result.")

        input("\nPress Enter to return to the media results...")

def search_nasa_media_library():
    """Search NASA's Image and Video Library repeatedly."""

    while True:
        query = input(
            "\nEnter a NASA mission or topic, "
            "or press Enter to return: "
        ).strip()

        if query == "":
            return

        results = search_nasa_library(query)
        items = results.get("collection", {}).get("items", [])

        if not items:
            print("\nNo NASA media results found.")
            continue

        browse_nasa_media_results(items)

def browse_apod():
    """Browse NASA Astronomy Pictures of the Day by date."""

    while True:
        date = input(
            "\nEnter a date (YYYY-MM-DD), "
            "press Enter for today's picture, "
            "or type B to return: "
        ).strip()

        if date.lower() == "b":
            return

        if date == "":
            apod = get_apod()
        else:
            apod = get_apod(date)

        if apod is None:
            print("\nUnable to retrieve NASA Astronomy Picture of the Day.")
            print("Possible reasons:")
            print(" - The date is before June 16, 1995.")
            print(" - The date is invalid or in the future.")
            print(" - The NASA API is temporarily unavailable.")
            continue

        print("\nNASA Astronomy Picture of the Day")
        print("=" * 40)
        print(f"Title: {apod['title']}")
        print(f"Date : {apod['date']}")
        print()
        print(textwrap.fill(apod["explanation"], width=70))
        print()
        print(f"Media URL: {apod['url']}")
        print("=" * 40)

        open_media = input(
            "\nWould you like to open this media "
            "in your web browser? (y/n): "
        ).strip().lower()

        if open_media in ("y", "yes"):
            webbrowser.open(apod["url"])
            print("\nOpening media in your browser...")

        input("\nPress Enter to return to the APOD date prompt...")

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