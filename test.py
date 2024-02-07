from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re


def is_age_restricted_video(api_key, URL):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_id_match = re.search(r'(?:youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?v=|youtube\.com/\S*?[?&]v=|youtube\.com/\S*?embed/\S*?|youtube\.com/\S*?v=)([^"&?/ ]{11})', URL)
    
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
print(is_age_restricted_video("AIzaSyCkJnK85KSuBazYbH-N6s2Ja5DnIf-vs5Q", "https://www.youtube.com/watch?v=fYH8eSiOf5I&pp=ygUUYWdlIHJlc3RyaWN0ZWQgdmlkZW8%3D"))