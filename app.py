from flask import Flask, jsonify, request
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/get_room_details', methods=['GET'])
def get_room_details():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    with open('room_data.json') as f:
        rooms = json.load(f)

    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

    available_rooms = [
        room for room in rooms
        if room['IsAvailable']
        and start_date_obj <= datetime.strptime(room['AvailabilityDate'], '%Y-%m-%d') <= end_date_obj
    ]

    return jsonify(available_rooms)
if __name__ == "__main__":
    app.run(debug=True)
