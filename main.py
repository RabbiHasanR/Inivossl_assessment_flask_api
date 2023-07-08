from datetime import datetime, date
from flask import Flask, request, jsonify
from database import ( Reading, database, 
                      add_reading, get_reading )
from utils import ( convert_timestamp_to_iso, convert_isoformat_to_date_string, 
                   get_avg_power_reading )

app = Flask(__name__)


@app.route('/data', methods=['POST'])
def post_data():
    data = request.data.decode('utf-8')
    readings = data.strip().split('\n')

    for reading in readings:
        reading_data = reading.split()
        if len(reading_data) != 3:
            response = {'success': False, 'message': 'Malformed data'}
            return jsonify(response), 400

        try:
            time, name, value = reading_data
            iso_time = convert_timestamp_to_iso(int(time))
            new_reading = Reading(iso_time, name, float(value))
            key = f"{new_reading.time}_{new_reading.value}"
            add_reading(key, new_reading)
        except (ValueError, TypeError) as e:
            response = {'success': False, 'message': 'Malformed data'}
            return jsonify(response), 400

    response = {'success': True, 'message': 'Data stored successfully'}
    return jsonify(response), 201





@app.route('/data', methods=['GET'])
def get_data():
    from_date =convert_isoformat_to_date_string(request.args.get('from'))
    to_date = convert_isoformat_to_date_string(request.args.get('to'))

    if not from_date or not to_date:
        return 'Please provide both "from" and "to" parameters.', 400
    filtered_data = [
        reading.__dict__ for reading in database.values()
        if from_date <= convert_isoformat_to_date_string(reading.time) <= to_date
    ]

    avg_power_readings = get_avg_power_reading(filtered_data)

    result = filtered_data + avg_power_readings

    return jsonify(result)



if __name__ == '__main__':
    app.run()
