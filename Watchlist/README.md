# Watchlist
## Python Flask API 

👩‍💻 I use several streaming platforms to watch programmes, and it is becoming hard to keep track of everything I have on my list and what programmes I have already started but haven't finished yet. To address the issue, I decided to build a Flask application with API endpoints where the user can view their watchlist, add new programmes and check and update progress for series and films. At this stage, the user is not able to delete programmes as this is done by stored procedures in the Watchlist database once the progress is equal to the amount of total episodes for series or equal to the duration in minutes for films. 

🗄️ The Watchlist database consists of several tables containing details of the platforms, programmes, genres, cast and progress and related to one another primarily by programme ID. It also has various triggers used in combination with stored procedures to remove watched programmes from progress tables and flag them in the main programmes table. Additionaly, database contains queries to display shortest series, average length of films and total counts.

⏯️ To avoid data corruption, triggers and procedures are commented out in the file, and in order to run the code safely, I recommend executing commands and queries in blocks in order of their appearance in the file and running the code for creating triggers before running any stored procedures. Instructions and explanations are provided with the code as comments. If you are unable to run procedures removing data, please run the command to disable safe update mode in MySQL (provided with the code block). All procedure calls are embedded in transactions as a failsafe, so changes can be reverted.

📁 The application consists 5 files:

🗄️ **watchlist_db.sql** file contains the Watchlist database - please make sure to run the whole file before using the app (procedures and triggers are commented out for convenience)

🔐  **config.py** file contains USER, HOST and PASSWORD data to connect to MySQL Workbench - please add your MySQL password as working password has been removed for security purposes. Edit USER and HOST information if necessary.

🛠️ **utils.py** file contains functions and SQL queries to interact with the database as well as exception handling for erros occuring during these operations.

📬 **app.py** file contains the Flask app and API endpoints. URLs are provided to check the API, you might need to change the port number (URLs and if main == main in app.py and main.py) in case encoded port is already in use on your machine. Please run this file before running the main file.

💁  **main.py** is the client side of the app and contains functions to interact with user and Flask application. Run this file once app.py is running and follow the prompts in the console. The app starts with a welcome message and watchlist overview, followed by a series of prompts to check progress, add programmes and update progress. User input is validated throughout the run, the app prompts the user to try again until valid input is provided. Each new entry is displayed to the user, and finally, user is prompted to confirm they're finished working with the app, at which point the programme stops with a goodbye message.

❗ Please install the below components in your PyCharm terminal to run the application:

1. `pip install mysql-connector python`
2. `pip install flask`
3. `pip install requests`

💡 In future, I would like to expand the project to add more functionality, i.e. upcoming seasons and sequels, ratings, recommendations, etc.

🍿 Please feel free to add any recommendations to the Watchlist :)
