# Dung Nguyen CIS 261 Country
# Part 2: Prepopulate the dictionary
# The dictionary is global for ease of access within the main script scope.
# A function would typically return this dictionary if encapsulated.
countries = {
    "USA": "United States of America",
    "CAN": "Canada",
    "MEX": "Mexico"
}

# Part 1: Function to display the heading and menu choices
def display_menu():
    """Displays the main menu options to the user."""
    print("----- Command Menu -----")
    print("V - View a country")
    print("A - Add a country")
    print("D - Delete a country")
    print("E - Exit the program")
    print("------------------------")

# Part 3: Functions to perform specific functionality
def view_country(country_dict):
    """Allows the user to view a country by its key."""
    print("\nAvailable country keys:")
    for key in country_dict:
        print(key, end=" ")
    print("\n")

    key = input("Enter a country key (e.g., USA): ").upper()
    if key in country_dict:
        print(f"Country: {country_dict[key]}\n")
    else:
        print(f"Error: '{key}' is an invalid key.\n")

def add_country(country_dict):
    """Allows the user to add a new country to the dictionary."""
    key = input("Enter a new country key (e.g., JPN): ").upper()
    if key in country_dict:
        print(f"Error: '{key}' already exists.\n")
    else:
        name = input(f"Enter the name for {key}: ")
        country_dict[key] = name
        print(f"'{name}' successfully added.\n")

def delete_country(country_dict):
    """Allows the user to delete a country from the dictionary."""
    key = input("Enter the key of the country to delete: ").upper()
    if key in country_dict:
        del country_dict[key]
        print(f"'{key}' successfully deleted.\n")
    else:
        print(f"Error: '{key}' is an invalid key.\n")

# Main program loop
def main():
    """Main program logic to interact with the user menu."""
    while True:
        display_menu()
        choice = input("Enter your command: ").upper()

        if choice == 'V':
            view_country(countries)
        elif choice == 'A':
            add_country(countries)
        elif choice == 'D':
            delete_country(countries)
        elif choice == 'E':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Error: Invalid command. Please try again.\n")

# Entry point for the script
if __name__ == "__main__":
    main()
