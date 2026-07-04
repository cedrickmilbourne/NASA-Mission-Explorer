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
        print("3. Exit")
        print()

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            show_featured_missions()
        elif choice == "2":
            print("\nSearch coming soon!\n")

        elif choice == "3":
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


if __name__ == "__main__":
    main()