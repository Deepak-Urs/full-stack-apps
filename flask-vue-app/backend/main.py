from flask import Flask, jsonify, request
from flask_cors import CORS

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
    'played': True
},
    {
    'title': 'Evil Within',
    'genre': 'Sports',
    'played': True
},
    {
    'title': 'The last of us',
    'genre': 'Sports',
    'played': False
},
    {
    'title': 'Days gone',
    'genre': 'Sports',
    'played': False
}]


@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}   

    if request.method == 'POST':
        print('POST Method calling')
        post_data = request.get_json()
        GAMES.append({
            'title': post_data('title'),
            'genre': post_data('genre'),
            'played': post_data('played')
        })
        response_object['message']='Game Added!'
    else:
        print('GET Method calling')
        response_object['games'] = GAMES

    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
