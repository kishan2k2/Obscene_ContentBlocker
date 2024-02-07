from flask import Flask, request, jsonify
from check import staticCheck, youtube, scrapable, age_restricted
app = Flask(__name__)

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    if staticCheck(url):
        result = jsonify({"Result": True})
    elif youtube(url):
        if age_restricted(url):
            result = jsonify({"Result": True})
        else:
            pass
    elif scrapable(url):
        pass
    else:
        result = jsonify({"Result": True})
    return result