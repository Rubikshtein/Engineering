from flask import Flask, jsonify, request
from utils import get_all_programmes, get_progress_films, get_progress_series, add_programme, update_series, update_film

# Create Flask app instance
app = Flask(__name__)

# Welcome endpoint - returns welcome message
@app.route('/')
def hello():
    return 'Welcome to your watchlist!'

# http://localhost:5002

# Endpoint to get an overview of all programmes - returns JSON response
@app.route('/programmes')
def get_programmes():
    res = get_all_programmes()
    return jsonify(res)

# http://localhost:5002/programmes

# Endpoint to get all films progress - returns JSON response
@app.route('/progress_films')
def get_films():
    res = get_progress_films()
    return jsonify(res)

# http://localhost:5002/progress_films

# Endpoint to get all series progress - returns JSON response
@app.route('/progress_series')
def get_series():
    res = get_progress_series()
    return jsonify(res)

# http://localhost:5002/progress_series

# Endpoint to add a new programme to the watchlist - POST
@app.route('/programmes', methods=['POST'])
def add_new_programme():
    programme_to_add = request.get_json()
    programme_name = programme_to_add['programme_name']
    programme_type = programme_to_add['programme_type']
    add_programme(
        programme_name=programme_to_add['programme_name'],
        programme_type=programme_to_add['programme_type'],
    )
    return "Added"

# http://localhost:5002/programmes

# Endpoint to update series progress - POST
@app.route('/progress_series', methods=['POST'])
def add_progress_series():
    series_to_update = request.get_json()
    programme_name = series_to_update['series_name']
    episodes_watched = series_to_update['episodes']
    update_series(
        programme_name=series_to_update['series_name'],
        episodes_watched=series_to_update['episodes'],
    )
    return "Progress series updated"

# http://localhost:5002/progress_series

# Endpoint to update films progress - POST
@app.route('/progress_films', methods=['POST'])
def add_progress_film():
    film_to_update = request.get_json()
    programme_name = film_to_update['film_name']
    minutes_watched = film_to_update['minutes']
    update_film(
        programme_name=film_to_update['film_name'],
        minutes_watched=film_to_update['minutes']
    )
    return "Progress films updated"

# http://localhost:5002/progress_films

# Run Flask app in debug mode on port 5002
if __name__ == '__main__':
    app.run(debug=True, port=5002)