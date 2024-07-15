# CFG-Assignments
## Forth Assignment - Watchlist API

For this assignment, I have decided to utilise the watchlist database built for the previous assignment and develop it into an API.
There are 5 files for this project:
watchlist_db.sql contains teh watchlist database
config.py contains USER, HOST and PASSWORD to connect to MySQL - please insert your password as mine has been removed for security purposes.
utils.py contains functions to interact with the database.
app.py contains Flask app and endpoints
main.py is the client side and contains functions to interact with user and Flask.
config file
add password to connect to MySQL
change port in the url
install mysql connector, flask and requests
You might need to change the port number in urls (main,app) and if name == main if port 5002 is in use on your machine.