import re
from config import Youtube_data_API
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
def staticCheck(url):
    pass

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
    pass