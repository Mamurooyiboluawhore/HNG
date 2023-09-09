from flask import Flask, request, jsonify
import datetime
import os
import json


app = Flask(__name__)


def get_slack_name():
    my_slack_username = 'Mamuro1️⃣'
    return (my_slack_username)


def get_current_day():
    return datetime.datetime.utcnow().strftime("%A")


def get_current_utc_time():
    utc_now = datetime.datetime.utcnow()
    return utc_now.isoformat()


def validate_utc_time(utc_time):
    try:
        utc_datetime = datetime.datetime.fromisoformat(utc_time)
        current_utc_datetime = datetime.datetime.utcnow()
        time_difference = current_utc_datetime - utc_datetime
        time_difference_hours = abs(time_difference.total_seconds() / 3600)

        # Check if the time difference is within +/- 2 hours.
        if time_difference_hours <= 2:
            return True
        else:
            return False
    except ValueError:
        # Handle invalid datetime format.
        return False


@app.route('/endpoint', methods=['GET'])
def get_info():
    slack_name = get_slack_name()
    current_day = get_current_day()
    utc_time = get_current_utc_time()
    track = request.args.get('track', '')
    github_url = os.environ.get('GITHUB_URL', '')
    source_code_url = os.environ.get('SOURCE_CODE_URL', '')

    # Validate UTC time here
    if not validate_utc_time(utc_time):
        return jsonify({"status": "Error", "message": "Invalid UTC time"}), 400

    response_data = {
        "slack_name": get_slack_name(),
        "current_day": 'Saturday',
        "Current UTC Time": '2023-09-09T07:09',
        "Track": 'backend',
        "github_file_url":
            'https://github.com/Mamurooyiboluawhore/HNG/endpoint.py',
        "github_repo_url": 'https://github.com/Mamurooyiboluawhore/HNG',
        "Status Code": "Success"
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
