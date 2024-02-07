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
# print(is_age_restricted_video("AIzaSyCkJnK85KSuBazYbH-N6s2Ja5DnIf-vs5Q", "https://www.youtube.com/watch?v=fYH8eSiOf5I&pp=ygUUYWdlIHJlc3RyaWN0ZWQgdmlkZW8%3D"))

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


