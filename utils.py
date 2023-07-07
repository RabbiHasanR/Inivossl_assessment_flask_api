from datetime import datetime


def convert_timestamp_to_iso(timestamp):
    timestamp = 1649941817
    dt = datetime.fromtimestamp(timestamp)
    iso_format = dt.isoformat()
    return iso_format