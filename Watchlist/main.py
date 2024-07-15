from pprint import pprint
import requests
import json

# Function to get an overview programmes from the database - Flask & user interaction
def get_overview():
    result = requests.get('http://localhost:5002/programmes')
    return result.json()

# Function to display films progress from the db - Flask & user interaction
def show_progress_films():
    result = requests.get('http://localhost:5002/progress_films')
    return result.json()

# Function to display series progress from the db - Flask & user interaction
def show_progress_series():
    result = requests.get('http://localhost:5002/progress_series')
    return result.json()

# Function to insert a new programme into the db - Flask & user interaction
def insert_new_programme(programme_name, programme_type):
    programme_to_add = {
        'programme_name': programme_name,
        'programme_type': programme_type
    }

    response = requests.post(
        'http://localhost:5002/programmes',
        headers={'content-type': 'application/json'},
        data=json.dumps(programme_to_add)
    )

# Function to update series progress in the db - Flask & user interaction
def update_progress_series(series_name, episodes):
    series_to_update = {
        'series_name': series_name,
        'episodes': episodes
    }

    response = requests.post(
        'http://localhost:5002/progress_series',
        headers={'content-type': 'application/json'},
        data=json.dumps(series_to_update)
    )

# Function to update films progress in the db - Flask & user interaction
def update_progress_films(film_name, minutes):
    film_to_update = {
        'film_name': film_name,
        'minutes': minutes
    }

    response = requests.post(
        'http://localhost:5002/progress_films',
        headers={'content-type': 'application/json'},
        data=json.dumps(film_to_update)
    )

# Main function to interact with user
def run():
    # Welcome message
    print('Welcome to your watchlist!')

    # finished flag is set to false to control the main loop
    finished = False
    while not finished:
        print('Here\'s an overview of your watchlist:')

        # Fetch watchlist overview - calls get overview function
        overview = get_overview()

        # Print overview
        pprint(overview)

        while True:
            # Ask user if they want to check progress - y/n
            check_progress = input('Would you like to check your progress (y/n)? ').lower()
            if check_progress == 'y':
                while True:
                    # If yes, prompt user to select programme type - f/s
                    choice = input('Would you like to check films or series (f/s)? ').lower()
                    if choice == 'f':
                        # Fetch and print films progress - calls show progress films function
                        films = show_progress_films()
                        pprint(films)

                    elif choice == 's':
                        # Fetch and print series progress - calls show progress series function
                        series = show_progress_series()
                        pprint(series)

                    else:
                        # Validate user input - prompt to answer again
                        print('Invalid input, please try again.')
                        continue

                    while True:
                        # Ask user if they want to continue checking progress - y/n
                        continue_check = input("Would you like to continue checking progress (y/n)? ").lower()
                        if continue_check == 'n':
                            break

                        # Validate user input
                        elif continue_check not in ['y', 'n']:
                            print('Invalid input, please try again.')

                        # Break loop
                        else:
                            break

                    # Break loop if user doesn't want to continue checking progress
                    if continue_check == 'n':
                        break

            # Break loop if user doesn't want to check progress
            elif check_progress == 'n':
                break

            # Validate user input
            else:
                print('Invalid input, please try again.')

        while True:
            # Ask user if they want to add a new programme - y/n
            add_new = input('Would you like to add a new programme (y/n)? ').lower()
            if add_new == 'y':
                while True:
                    # Get user input for programme name
                    programme_name = input("Add programme name ('The boys'): ")
                    # Get user input for programme type
                    programme_type = input("Add programme type ('film/series'): ")
                    # Add new programme - calls insert new programme function
                    insert_new_programme(programme_name, programme_type)
                    # Print message for the user if successful entry
                    print('Watchlist successfully updated!')
                    # Fetch watchlist overview - calls get overview function
                    overview = get_overview()
                    # Print updated watchlist overview
                    pprint(overview)

                    while True:
                        # Ask user if they want to add another programme - y/n
                        add_more_programmes = input("Would you like to add more programmes (y/n)? ").lower()
                        # Break loop if no
                        if add_more_programmes == 'n':
                            break

                        # Validate user input
                        elif add_more_programmes not in ['y', 'n']:
                            print('Invalid input, please try again.')
                        # Break loop
                        else:
                            break

                    # Break loop if user doesn't want to continue adding programmes
                    if add_more_programmes == 'n':
                        break

            # Break loop if user doesn't want to add programmes
            elif add_new == 'n':
                break

            # Validate user input
            else:
                print('Invalid input, please try again.')

        while True:
            # Ask user if they want to update their programmes progress - y/n
            add_progress = input('Would you like to update your progress (y/n)? ').lower()
            if add_progress == 'y':
                while True:
                    # If yes, prompt user to select programme type - f/s
                    programme_type = input("Would you like to update films or series (f/s)? ").lower()
                    if programme_type == 'f':
                        while True:
                            # Get user input for film name
                            film_name = input("Add film name ('Atlas'): ")
                            # Get user input for minutes watched
                            minutes = float(input("How many minutes have you watched (num)? "))
                            # Update film progress - calls update progress films function
                            update_progress_films(film_name, minutes)
                            # Fetch all films progress
                            films = show_progress_films()
                            # Print all films progress
                            pprint(films)

                            while True:
                                # Ask if user wants to continue updating films progress
                                update_more_films = input("Would you like to update more films (y/n)? ").lower()
                                # Break loop if no
                                if update_more_films == 'n':
                                    break

                                # Validate user input
                                elif update_more_films not in ['y', 'n']:
                                    print('Invalid input, please try again.')

                                # Break loop
                                else:
                                    break

                    elif programme_type == 's':
                        while True:
                            # Get user input for series name
                            series_name = input("Add series name ('Baby Reindeer'): ")
                            # Get user input for episodes watched
                            episodes = float(input("How many episodes have you watched (num)? "))
                            # Update series progress - calls update progress series
                            update_progress_series(series_name, episodes)
                            # Fetch  all series progress
                            series = show_progress_series()
                            # Print all series progress
                            pprint(series)

                            while True:
                                # Ask if user wants to continue updating series progress
                                update_more_series = input("Would you like to update more series (y/n)? ").lower()
                                # Break loop if no
                                if update_more_series == 'n':
                                    break

                                # Validate user input
                                elif update_more_series not in ['y', 'n']:
                                    print('Invalid input, please try again.')

                                # Break loop
                                else:
                                    break

                            # Break loop if user doesn't want to continue updating series progress
                            if update_more_series == 'n':
                                break
                    # Validate user input
                    else:
                        print('Invalid input, please try again.')

                    while True:
                        # Ask user if they want to continue updating progress
                        continue_update = input('Would you like to continue updating progress (y/n)? ').lower()
                        # Break loop if no
                        if continue_update == 'n':
                            break

                        # Validate user input
                        elif continue_update not in ['y', 'n']:
                            print('Invalid input, please try again.')

                        # Break loop
                        else:
                            break
                    # Break loop if user doesn't want to continue updating progress
                    if continue_update == 'n':
                        break

            # Break loop if user doesn't want to add progress
            elif add_progress == 'n':
                break

            # Validate user input
            else:
                print('Invalid input, please try again.')

        while True:
            # Ask user if they are finished with their watchlist - y/n
            finished = input("Are you finished (y/n)? ").lower()

            if finished == 'y':
                # If yes, set finished flag to true to break the main loop and exit function
                finished = True
                break

            elif finished == 'n':
                # If no, main loop continues
                finished = False
                break

            # Validate user input
            else:
                print('Invalid input, please try again.')

        # Goodbye message
        print("See you later!")



if __name__ == '__main__':
    run()


