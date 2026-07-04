"""
NASA Missions Explorer

Author: Cedrick D. Milbourne

Explore NASA missions using Python.
"""

from missions import MISSIONS

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
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_featured_missions()
        elif choice == "2":
            search_missions()

        elif choice == "3":
            filter_by_destination()

        elif choice == "4":
            search_by_launch_year()

        elif choice == "5":
            print("\nThank you for using NASA Missions Explorer.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


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

    print("\n" + "=" * 40)
    print(mission["name"])
    print("=" * 40)
    print(f"Launch Year : {mission['year']}")
    print(f"Destination : {mission['destination']}")
    print(f"Purpose     : {mission['purpose']}")
    print("=" * 40)
    print()
    input("Press Enter to return to the main menu...")


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
        ):
            print(mission["name"])
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

if __name__ == "__main__":
    main()