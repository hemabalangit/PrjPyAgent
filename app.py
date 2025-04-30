from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Agent Success"})

@app.route('/api/agent', methods=['GET'])
def agent():
    return jsonify({"message": "Success!"})

if __name__ == '__main__':
    app.run(debug=True)
