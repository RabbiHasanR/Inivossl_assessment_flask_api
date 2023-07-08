from datetime import datetime
from collections import defaultdict


def convert_timestamp_to_iso(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    iso_format = dt.isoformat()
    return iso_format

def convert_isoformat_to_date_string(isodate):
    return datetime.fromisoformat(isodate).date()


def get_avg_power_reading(filtered_data):
    power_reading_hash_map =defaultdict(list)
    current_reading_hash_map = defaultdict(list)

    for reading in filtered_data:
        if reading['name'].lower() == 'power':
            if reading['time'] in power_reading_hash_map:
                power_reading_hash_map[reading['time']].append(reading['value'])
            else:
                power_reading_hash_map[reading['time']].append(reading['value'])
        
        elif reading['name'].lower() == 'current':
            if reading['time'] in current_reading_hash_map:
                current_reading_hash_map[reading['time']].append(reading['value'])
            else:
                current_reading_hash_map[reading['time']].append(reading['value'])
        else:
            continue

    result = []
    for key, items in power_reading_hash_map.items():
        power_avg = sum(items) / len(items) if items else 0
        currennt_items = current_reading_hash_map.get(key, [])
        current_avg = sum(currennt_items) / len(currennt_items) if currennt_items else 0
        avg_power_reading = power_avg * current_avg

        result.append({
            'date': key,
            'average_power_reading': avg_power_reading
        })

    return result
