from datetime import datetime, date
from flask import Flask, request, jsonify
from database import Reading, database, add_reading, get_reading
from utils import convert_timestamp_to_iso

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
            print("new reading timestamp:", new_reading.time)
            add_reading(key, new_reading)
        except (ValueError, TypeError) as e:
            print("except error:", e)
            response = {'success': False, 'message': 'Malformed data'}
            return jsonify(response), 400

    response = {'success': True, 'message': 'Data stored successfully'}
    return jsonify(response), 201



def avg_power_reading(filtered_data):
    result = []
    current_sum = 0
    power_sum = 0
    count = 0
    prev_date = None

    for reading in filtered_data:
        date = reading['time']
        if prev_date is None:
            prev_date = date

        if date != prev_date:
            if count > 0:
                avg_current = current_sum / count
                avg_power = power_sum / count
                avg_power_reading = avg_current * avg_power

                result.append({
                    'date': prev_date,
                    'average_power_reading': avg_power_reading
                })

            current_sum = 0
            power_sum = 0
            count = 0
            prev_date = date

        current_sum += reading['value'] if reading['name'].lower() == 'current' else 0
        power_sum += reading['value'] if reading['name'].lower() == 'power' else 0
        count += 1

    if count > 0:
        avg_current = current_sum / count
        avg_power = power_sum / count
        avg_power_reading = avg_current * avg_power

        result.append({
            'date': prev_date,
            'average_power_reading': avg_power_reading
        })
    return result

@app.route('/data', methods=['GET'])
def get_data():
    from_date = date.fromisoformat(request.args.get('from'))
    to_date = date.fromisoformat(request.args.get('to'))
    if not from_date or not to_date:
        return 'Please provide both "from" and "to" parameters.', 400
    filtered_data = [
        get_reading(key).__dict__ for key, reading in database.items()
        if from_date <= datetime.fromisoformat(reading.time).date() <= to_date
    ]

    print('filtered data:', filtered_data)
    
    avg_power_reading_list = avg_power_reading(filtered_data)

    
    print('avg power reading list:', avg_power_reading_list)


    return jsonify(filtered_data + avg_power_reading_list)



if __name__ == '__main__':
    app.run()
