import os
from flask import Flask, request, jsonify
from app.CallFuctions.check import staticCheck, youtube, scrapable, age_restricted, caption_check, Safe_browsing
from app.CallFuctions.scrape import youtube_caption, article_scrape
from app.CallFuctions.preprocess import data_preprocessing
from app.CallFuctions.ML import huggingface
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import warnings
warnings.filterwarnings("ignore")
app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    id = data.get('id')
    url = data.get('url')
    reciever_mail = data.get('email')
    sender_email = "payadikishan@gmail.com"
    password = os.environ.get("password")
    body = f'User {id} is trying to acess {url} instead of warning of obscene content'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciever_mail
    message['Subject'] = f'Suspicious activity of user ID {id}'
    message.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_mail, message.as_string())
        return jsonify({"Result": True})
    return jsonify({"Result": False})


@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    elif not Safe_browsing(url):
        result = jsonify({"Result": True})
    elif staticCheck(url):
        result = jsonify({"Result": True}) 
    elif youtube(url):
        if age_restricted(url):
            result = jsonify({"Result": True})
        elif caption_check(url):
            data = youtube_caption(url)
            data = data_preprocessing(data) 
            # if staticCheck2(data):
            #     return jsonify({"Result": True})
            # return jsonify({"Result": False})
            return huggingface(data)
        else:
            return jsonify({"Result":False})
    elif scrapable(url):
        data = article_scrape(url)
        data = data_preprocessing(data) 
        # if staticCheck2(data):
        #     return jsonify({"Result": True})
        # return jsonify({"Result": False})
        return huggingface(data)
    else:
        result = jsonify({"Result": False})
    return result
