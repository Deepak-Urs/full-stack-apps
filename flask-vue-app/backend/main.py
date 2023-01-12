from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {'origins': "*"}})
# CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers":"Access-Control-Allow-Origin"}})

# hello world route


@app.route('/', methods=['GET'])
def greetings():
    return ("hello World!")


@app.route('/shark', methods=['GET'])
def shark():
    return ("Shark!")


GAMES = [{
    'title': '2k21',
    'genre': 'Sports',
    'played': True,
    'id': uuid.uuid4().hex
},
    {
    'title': 'Evil Within',
    'genre': 'Sports',
    'played': True,
    'id': uuid.uuid4().hex
},
    {
    'title': 'The last of us',
    'genre': 'Sports',
    'played': False,
    'id': uuid.uuid4().hex
},
    {
    'title': 'Days gone',
    'genre': 'Sports',
    'played': False,
    'id': uuid.uuid4().hex
}]


# The GET and POST handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}   

    if request.method == 'POST':
        print('POST Method calling')
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data['title'],
            'genre': post_data['genre'],
            'played': post_data['played']
        })
        response_object['message']='Game Added!'
    else:
        print('GET Method calling')
        response_object['games'] = GAMES

    return jsonify(response_object)

# The PUT and DELETE handler
@app.route('/games/<game_id>', methods = ['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data['title'],
            'genre': post_data['genre'],
            'played': post_data['played']
        })
        response_object['message'] = 'Game Updated!'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game removed!'
    return jsonify(response_object)

# Removing the game and updating
def remove_game(game_id):
    for game in GAMES:
        if game['id'] == 'game_id':
            GAMES.remove(game)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
