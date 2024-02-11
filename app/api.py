from flask import Flask, request, jsonify
from app.CallFuctions.check import staticCheck, youtube, scrapable, age_restricted, caption_check, Safe_browsing, staticCheck2
from app.CallFuctions.scrape import youtube_caption, article_scrape
from app.CallFuctions.preprocess import data_preprocessing
from app.CallFuctions.ML import huggingface
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    elif not Safe_browsing(url):
        result = jsonify({"Result": True})
    elif staticCheck(url):
        result = jsonify({"Result": True}) # See if I can use the safe browser API
    elif youtube(url):
        if age_restricted(url):
            result = jsonify({"Result": True})
        elif caption_check(url):
            data = youtube_caption(url)
            data = data_preprocessing(data) # Confirm the format of the input data for preprocessing.
            # if staticCheck2(data):
            #     return jsonify({"Result": True})
            return huggingface(data)
        else:
            return jsonify({"Result":False})
    elif scrapable(url):
        data = article_scrape(url)
        data = data_preprocessing(data) # Confirm the format of the input data for preprocessing.
        # if staticCheck2(data):
        #     return jsonify({"Result": True})
        # return data
        return huggingface(data)
    else:
        result = jsonify({"Result": False})
    return result
