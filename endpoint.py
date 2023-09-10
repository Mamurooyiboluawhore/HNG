from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

def get_current_day():
    current_day = datetime.datetime.utcnow().strftime("%A")
    time = datetime.datetime.utcnow()
    utc_now = time.isoformat()
    return current_day, utc_now

@app.route('/endpoint', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name', '')
    track = request.args.get('track', '')
    current_day, utc_now = get_current_day()

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_now,
        "track": track,
        "github_file_url":
            'https://github.com/Mamurooyiboluawhore/HNG/endpoint.py',
        "github_repo_url": 'https://github.com/Mamurooyiboluawhore/HNG',
        "status_code": 200
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
