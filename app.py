from flask import Flask, jsonify, request
from move import Move
from battlesnakerequest import BattleSnakeRequest

app = Flask(__name__)

@app.route('/')
def info():
    return jsonify({
        "apiversion": "1",
        "author": "John Boctor",
        "color": "#228C22",
        "head": "silly",
        "tail": "sharp",
        "version": "0.0.1-beta",
    })

@app.route('/start', methods = ['POST'])
def start():
    return jsonify()

@app.route('/end', methods = ['POST'])
def end():
    return jsonify()

@app.route('/move', methods = ['POST'])
def index():
    battle_snake_request = BattleSnakeRequest(request.json)
    move = Move(battle_snake_request.getSnake(), battle_snake_request.getBoard())
    response = {"move": move.getMove()}
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
