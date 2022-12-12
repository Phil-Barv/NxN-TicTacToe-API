from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import check_win

app = Flask(__name__)
cors = CORS(app)

from game import TicTacToe

import ast

@app.route('/', methods=["GET"])
def index():
    try:
        if a:
            board = a.board
    except:
        board = TicTacToe(2).board

    return jsonify({"state": board})

@app.route('/get-board', methods=["POST"])
def get_board():
    data = request.get_json()
    data = int(data['size'])
    global a
    a = TicTacToe(data, create_PD=True)

    return jsonify({"state": a.board})

@app.route('/human-play', methods=["POST"])
def human_play():
    data = request.get_json()
    res = a.play_human(data["state"], data["pos"], data["value"])
    # print("\n\n\nHuman", res)
 
    return jsonify({"state": res, "win": check_win(res)})

@app.route('/ai-play', methods=["POST"])
def ai_play():
    data = request.get_json()

    if str(data["state"]) in TicTacToe.pattern_database.keys():
        res = TicTacToe.pattern_database[str(data["state"])]
        # res = ast.literal_eval(res)
        print("\n\nAI-PD", res, "\n")

        return jsonify({"state": res, "win": check_win(res)})

    else:
        #hold state
        state = str(data['state'])
        # print("STATE", state)

        #generate next move
        res = a.play_ai(data["state"], data["value"], data["strategy"])
        print("\n\nAI-MM", res, "\n")

        #update PD
        if res and state:
            TicTacToe.pattern_database[state] = res
            # print("\nInserted", TicTacToe.pattern_database[state])
            print(f"Inserted new entry\nDatabase Size {len(TicTacToe.pattern_database)}\n")
    
        return jsonify({"state": res, "win": check_win(res)})

if __name__ == "__main__":
    print("Starting server...")
    # global a
    # a = TicTacToe(3, create_PD=True)
    app.run(debug=True)
