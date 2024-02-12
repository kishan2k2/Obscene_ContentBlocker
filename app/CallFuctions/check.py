import re
import os
import json
# from app.CallFuctions.config import Youtube_data_API, SafeBrowsing_API_KEY, block_words, check_word
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import requests
from newspaper import Article, ArticleException
import warnings
warnings.filterwarnings("ignore")
Youtube_data_API = os.environ.get("Youtube_data_API")
SafeBrowsing_API_KEY = os.environ.get("SafeBrowsing_API_KEY")
block_words = os.environ.get("block_words")
def staticCheck(url):
    if any(re.search(keyword, url, re.IGNORECASE) for keyword in block_words):
        return True
    else:
        return False
def youtube(url):
    youtube_patterns = [
        r'^https?://(www\.)?youtube\.com/watch\?v=',
        r'^https?://youtu\.be/'
    ]
    for pattern in youtube_patterns:
        if re.match(pattern, url):
            return True
        else:
            False

def age_restricted(url):
    youtube = build('youtube', 'v3', developerKey=Youtube_data_API)
    video_id_match = re.search(r'(?:youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?v=|youtube\.com/\S*?[?&]v=|youtube\.com/\S*?embed/\S*?|youtube\.com/\S*?v=)([^"&?/ ]{11})', url)
    
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        print("Invalid YouTube URL")
        return False
    try:
        video_response = youtube.videos().list(
            part='contentDetails',
            id=video_id
        ).execute()

        content_details = video_response['items'][0]['contentDetails']
        content_rating = content_details.get('contentRating', {})

        # Check if the video is age-restricted
        if content_rating.get('ytRating') == 'ytAgeRestricted':
            return True
        else:
            return False

    except HttpError as e:
        print(f'Error retrieving video details: {e}')
        return False

def scrapable(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("False")
        return False

    article = Article(url)

    article.download()
    try:
        article.parse()
    except ArticleException as e:
        print("False")
        return False

    # Access the article content
    article_text = article.text
    if len(article_text)==0:
        print("False")
        return False
    return True

def caption_check(url):
    video_id_match = re.search(r'(?:youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?v=|youtube\.com/\S*?[?&]v=|youtube\.com/\S*?embed/\S*?|youtube\.com/\S*?v=)([^"&?/ ]{11})', url)
    
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        print("Invalid YouTube URL")
        return False
    youtube = build('youtube', 'v3', developerKey=Youtube_data_API)
    try:
        captions_response = youtube.captions().list(
            part='snippet',
            videoId=video_id
        ).execute()

        captions = captions_response.get('items', [])
        print(captions)
        return len(captions) > 0

    except HttpError as e:
        print(f'Error checking captions: {e}')
        return False
    
def Safe_browsing(url):
    safe_browsing_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={SafeBrowsing_API_KEY}'
    payload = {
        'client': {
            'clientId': 'your-application-name',
            'clientVersion': '1.0.0',
        },
        'threatInfo': {
            'threatTypes': ['MALWARE', 'SOCIAL_ENGINEERING', 'UNWANTED_SOFTWARE', 'THREAT_TYPE_UNSPECIFIED'],
            'platformTypes': ['ANY_PLATFORM'],
            'threatEntryTypes': ['URL'],
            'threatEntries': [{'url': url}],
        },
    }
    headers = {'Content-Type': 'application/json'}

    response = requests.post(safe_browsing_url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        threat_matches = response.json().get('matches', [])
        if threat_matches:
            return False
        else:

            return True
    else:
        return True
    
def staticCheck2(data):
    for word in data:
        if word in check_word:
            print(word)
            return True