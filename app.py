from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

from game import TicTacToe

@app.route('/', methods=["GET"])
def index():
    try:
        if a:
            board = a.board
    except:
        board = TicTacToe(0).board

    return jsonify({"state": board})

@app.route('/get-board', methods=["POST"])
def get_board():
    data = request.get_json()
    data = int(data['size'])
    global a
    a = TicTacToe(data)

    return jsonify({"state": a.board, "win":a.check_win(a.board)})

@app.route('/human-play', methods=["POST"])
def human_play():
    data = request.get_json()
    res = a.play_human(data["pos"], data["value"])
    print("\n\n\nHuman", res)
 
    return jsonify({"state": res, "win":a.check_win(res)})

@app.route('/ai-play', methods=["POST"])
def ai_play():
    data = request.get_json()
    res = a.play_ai(data["state"], data["value"])
    print("\n\n\nAI", res)
    
    return jsonify({"state": res, "win": a.check_win(res)})

if __name__ == "__main__":
    app.run(debug=True)
