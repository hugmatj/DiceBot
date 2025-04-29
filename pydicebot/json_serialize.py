import datetime
import json

def to_date_string(dt):
    timestamp = int(dt.timestamp() * 1000) # Milliseconds
    return str(timestamp)

def to_datetime(milliseconds):
    try:
        return datetime.datetime.fromtimestamp(int(milliseconds) / 1000)
    except (ValueError, TypeError): # Handle parsing errors
        try:
            return datetime.datetime.fromisoformat(milliseconds.replace("Z", "+00:00")) # Handle ISO format
        except ValueError:
            return datetime.datetime(1970, 1, 1) # Return default date on failure

def current_date():
    timestamp = int(datetime.datetime.utcnow().timestamp() * 1000)
    return str(timestamp)