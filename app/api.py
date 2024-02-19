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
from flask_cors import  CORS, cross_origin
warnings.filterwarnings("ignore")
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADER'] = 'Content-Type'


@app.route('/send-email', methods=['POST'])
def send_email():
    print("send email has been invoked")
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
        return jsonify({"result": True})
    return jsonify({"result": False})


@app.route('/send-email-alert', methods=['POST'])
def send_email_2():
    print('send email 2 has been invoked')
    data = request.get_json()
    id = data.get('id')
    reciever_email = data.get('email')
    sender_email = 'payadikishan@gmail.com'
    password = os.environ.get('password')
    status = data.get('status')
    name = data.get('name')
    if name == 'OCB':
        body = f'User {id} has {status} Obscene content blocker extension'
    else:
        body = f'User {id} has {status} The management extension'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciever_email
    message['Subject'] = f'User {id} has changed the status of the browser extension'
    message.attach(MIMEText(body, 'plain'))
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, message.as_string())
        return jsonify({"result": True})
    return jsonify({'result': False})


@app.route('/check-url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    elif not Safe_browsing(url):
        result = jsonify({"result": True})
    elif staticCheck(url):
        result = jsonify({"result": True}) 
    elif youtube(url):
        print("Inside YT")
        if age_restricted(url):
            print("Inside Age resricted")
            result = jsonify({"result": True})
        elif caption_check(url):
            data = youtube_caption(url)
            data = data_preprocessing(data) 
            # if staticCheck2(data):
            #     return jsonify({"result": True})
            # return jsonify({"result": False})
            return huggingface(data)
        else:
            return jsonify({"result":False})
    elif scrapable(url):
        data = article_scrape(url)
        data = data_preprocessing(data) 
        # if staticCheck2(data):
        #     return jsonify({"result": True})
        # return jsonify({"result": False})
        return huggingface(data)
    else:
        result = jsonify({"result": False})
    return result
