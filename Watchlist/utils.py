import mysql.connector
from config import USER, HOST, PASSWORD

# Exception for database connection errors
class DbConnectionError(Exception):
    pass

# Function to establish db connection
def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

# Function to get all programmes from the db
def get_all_programmes():
    programmes = []
    try:
        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # SQL query to retrieve all programmes
        query = """SELECT * FROM Programme"""

        # Execute query
        cursor.execute(query)

        # Fetch all results from executed query
        result = cursor.fetchall()

        # Print each programme
        for i in result:
            print(i)

        # Store programmes information
        programmes = result

        # Close cursor connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Return programmes
    return programmes

# Function to retrieve films progress from the db
def get_progress_films():
    progress_films = []
    try:
        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # SQL query to retrieve films progress - joins related tables in the db
        query = """ 
        SELECT
        p.programme_name,
        pf.minutes_watched,
        f.duration_minutes
        FROM 
        Programme p
        JOIN
        Progress_Films pf ON p.programme_ID = pf.programme_ID
        JOIN
        Films f ON p.programme_ID = f.programme_ID;
        """

        # Execute query
        cursor.execute(query)

        # Fetch all results from executed query
        result = cursor.fetchall()

        # Print each film progress
        for i in result:
            print(i)

        # Store films progress
        progress_films = result

        # Close cursor connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Return films progress
    return progress_films

# Function to retrieve series progress from the db
def get_progress_series():
    progress_series = []
    try:
        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # # SQL query to retrieve series progress - joins related tables in the db
        query = """ 
        SELECT
        p.programme_name,
        ps.episodes_watched,
        s.total_episodes
        FROM 
        Programme p
        JOIN
        Progress_Series ps ON p.programme_ID = ps.programme_ID
        JOIN
        Series s ON p.programme_ID = s.programme_ID;
        """

        # Execute query
        cursor.execute(query)

        # Fetch all results from executed query
        result = cursor.fetchall()

        # Print each series progress
        for i in result:
            print(i)

        # Store series progress
        progress_series = result

        # Close cursor connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Return series progress
    return progress_series

# Function to add new programme to the db
# Takes programme name and type as parameters
def add_programme(programme_name, programme_type):
    try:
        # Validate programme type - only 'series' or 'films' allowed
        if programme_type not in ['series', 'film']:
            raise ValueError("programme_type not allowed")

        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # Print statement for debugging
        print(f'Programme Type: {programme_type}')

        # SQL query to insert new programme
        query = """
        INSERT INTO Programme 
        (programme_name, programme_type)
        VALUES (%s, %s)
        """

        # Print statement for debugging
        print(query)

        # Execute query with parameters
        cursor.execute(query, (programme_name, programme_type))

        # Commit transaction
        db_connection.commit()

        # Close cursor connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to insert data into DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Confirm data entry
    print("The record has been added to the DB")

# Function to update series progress in the db
# Takes programme name and episodes watched as parameters
def update_series(programme_name, episodes_watched):
    try:
        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # SQL query to retrieve programme ID
        query_1 = """
        SELECT
        p.programme_ID,
        p.programme_name,
        ps.episodes_watched,
        s.total_episodes
        FROM 
        Programme p
        JOIN
        Progress_Series ps ON p.programme_ID = ps.programme_ID
        JOIN
        Series s ON p.programme_ID = s.programme_ID
        WHERE p.programme_name = %s;
        """

        # Execute query with programme name
        cursor.execute(query_1, (programme_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Handle exception when programme not found in the db
        if not result:
            raise ValueError(f"Programme '{programme_name}' not found in your watchlist")

        # Store programme ID
        programme_ID = result[0]

        # SQL query to update series progress
        query_2 = """ 
        UPDATE Progress_Series
        SET episodes_watched = %s
        WHERE programme_ID = %s
        """

        # Execute query with episodes watched and programme ID
        cursor.execute(query_2, (episodes_watched, programme_ID))

        # Commit transaction
        db_connection.commit()

        # Close db connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to insert data into the DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Confirm data update
    print("The record has been updated")

# Function to update films progress in the db
# Takes programme name and minutes watched as parameters
def update_film(programme_name, minutes_watched):
    try:
        # Establish db connection
        db_name = 'WatchlistDB'
        db_connection = _connect_to_db(db_name)

        # Create a cursor object to interact with the db
        cursor = db_connection.cursor()
        print("Successfully connected to the DB: %s" % db_name)

        # SQL query to retrieve programme ID
        query_1 = """
        SELECT
        p.programme_ID,
        p.programme_name,
        pf.minutes_watched,
        f.duration_minutes
        FROM 
        Programme p
        JOIN
        Progress_Films pf ON p.programme_ID = pf.programme_ID
        JOIN
        Films f ON p.programme_ID = f.programme_ID
        WHERE p.programme_name = %s;
        """

        # Execute query with programme name
        cursor.execute(query_1, (programme_name,))

        # Fetch the result
        result = cursor.fetchone()

        # Handle exception if programme not found in the db
        if not result:
            raise ValueError(f"Programme '{programme_name}' not found in your watchlist")

        # Store programme ID
        programme_ID = result[0]

        # SQL query to update film progress
        query_2 = """ 
        UPDATE Progress_Films
        SET minutes_watched = %s
        WHERE programme_ID = %s
        """

        # Execute query with minutes watched and programme ID
        cursor.execute(query_2, (minutes_watched, programme_ID))

        # Commit transaction
        db_connection.commit()

        # Close db connection
        cursor.close()

    # Handle exceptions that occur during the db operation
    except Exception:
        raise DbConnectionError("Failed to insert data into the DB")

    # Close db connection
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    # Confirm data update
    print("The record has been updated")