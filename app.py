from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API!"})

@app.route('/api/agent', methods=['GET'])
def agent():
    return jsonify({"message": "Room Booked Successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
