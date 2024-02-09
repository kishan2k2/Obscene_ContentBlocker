# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# import re


# def is_age_restricted_video(api_key, URL):
#     youtube = build('youtube', 'v3', developerKey=api_key)
#     video_id_match = re.search(r'(?:youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?v=|youtube\.com/\S*?[?&]v=|youtube\.com/\S*?embed/\S*?|youtube\.com/\S*?v=)([^"&?/ ]{11})', URL)
    
#     if video_id_match:
#         video_id = video_id_match.group(1)
#     else:
#         print("Invalid YouTube URL")
#         return False
#     try:
#         video_response = youtube.videos().list(
#             part='contentDetails',
#             id=video_id
#         ).execute()

#         content_details = video_response['items'][0]['contentDetails']
#         content_rating = content_details.get('contentRating', {})

#         # Check if the video is age-restricted
#         if content_rating.get('ytRating') == 'ytAgeRestricted':
#             return True
#         else:
#             return False

#     except HttpError as e:
#         print(f'Error retrieving video details: {e}')
#         return False
# print(is_age_restricted_video("", "https://www.youtube.com/watch?v=&pp=ygUUYWdlIHJlc3RyaWN0ZWQgdmlkZW8%3D"))

# import requests
# from bs4 import BeautifulSoup
# from newspaper import Article, ArticleException
# def scrape_article(url):
#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code != 200:
#         print("False")
#         return None

#     article = Article(url)

#     article.download()
#     try:
#         article.parse()
#     except ArticleException as e:
#         print("False")
#         return False

#     # Access the article content
#     article_text = article.text
#     if len(article_text)==0:
#         print("False")
#         return False
#     return article_text

# # Example usage
# article_url = "https://ww3.readvinlandsaga.com/chapter/vinland-saga-chapter-194/"
# article_content = scrape_article(article_url)

# # Print the scraped content if available
# if article_content:
#     print(article_content)

# from newspaper import Article, ArticleException
# def scrape_article(url):
#     article = Article(url)

#     article.download()
#     try:
#         article.parse()
#     except ArticleException as e:
#         print("False")
#         return False

#     # Access the article content
#     article_text = article.text
#     return article_text
# data = scrape_article("https://www.news18.com/world/rebuild-injured-pakistan-nawaz-sharif-claims-victory-in-polls-invites-all-parties-to-form-coalition-govt-8773185.html")
# print(data)

# from youtube_transcript_api import YouTubeTranscriptApi
# if not YouTubeTranscriptApi.get_transcript('F3c0AcfPwd'):
#     print("NA")

# import googleapiclient.discovery
# from googleapiclient.errors import HttpError

# def has_captions(api_key, video_id):
#     youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

#     try:
#         captions_response = youtube.captions().list(
#             part='snippet',
#             videoId=video_id
#         ).execute()

#         captions = captions_response.get('items', [])
#         print(captions)
#         return len(captions) > 0

#     except HttpError as e:
#         print(f'Error checking captions: {e}')
#         return False

# # Example usage
# api_key = ''
# video_id = 'OZRYzH0Q0pU'

# result = has_captions(api_key, video_id)

# if result:
#     print("The video has captions.")
# else:
    # print("The video does not have captions.")
