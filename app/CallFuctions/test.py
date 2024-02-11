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

# import requests
# import json

# from config import SafeBrowsing_API_KEY
# api_key = SafeBrowsing_API_KEY

# def check_url_safe_browsing(api_key, url):
#     safe_browsing_url = f'https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}'
#     print('hi')
#     payload = {
#         'client': {
#             'clientId': 'your-application-name',
#             'clientVersion': '1.0.0',
#         },
#         'threatInfo': {
#             'threatTypes': ['MALWARE', 'SOCIAL_ENGINEERING', 'UNWANTED_SOFTWARE', 'THREAT_TYPE_UNSPECIFIED'],
#             'platformTypes': ['ANY_PLATFORM'],
#             'threatEntryTypes': ['URL'],
#             'threatEntries': [{'url': url}],
#         },
#     }
#     print('hi')
#     headers = {'Content-Type': 'application/json'}

#     response = requests.post(safe_browsing_url, data=json.dumps(payload), headers=headers)

#     if response.status_code == 200:
#         threat_matches = response.json().get('matches', [])
#         if threat_matches:
#             return False
#         else:

#             return True
#     else:
#         # User ko benifit of the doubt dene ke liye
#         return True

# Example usage
# api_key = 'YOUR_API_KEY'
# url_to_check = ''

# check_url_safe_browsing(api_key, url_to_check)



# import re

# def is_explicit_content(url):
#     # Define explicit content keywords
#     explicit_keywords = ['adult', 'explicit', 'porn', 'xxx']

#     # Check if any keyword is present in the URL
#     if any(re.search(keyword, url, re.IGNORECASE) for keyword in explicit_keywords):
#         return True
#     else:
#         return False

# # Example usage
# url_to_check = 'https://example.com/adult-content'
# result = is_explicit_content(url_to_check)

# if result:
#     print("The URL contains explicit content.")
# else:
#     print("The URL is safe.")
# import nltk
# from nltk.stem.porter import PorterStemmer
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# import string
# import re

# translator = str.maketrans('', '', string.punctuation)
# stemmer = PorterStemmer()
# stop_words = set(stopwords.words("english"))

# def read_data_from_file(file_path):
#     with open(file_path, 'r') as file:
#         data = file.readlines()
#     return data

# def write_data_to_file(file_path, data):
#     with open(file_path, 'w') as file:
#         for line in data:
#             file.write(line)

# def data_preprocessing(data):
#     preprocessed_data = []
#     for line in data:
#         line = line.lower()
#         line = re.sub(r'\d+', '', line)
#         line = line.translate(translator)
#         line = " ".join(line.split())
#         line = word_tokenize(line)
#         stem = [stemmer.stem(word) for word in line]
#         line = [word for word in stem if word not in stop_words]
#         preprocessed_data.append(" ".join(line))  # Append the preprocessed line to the list
#     return preprocessed_data

# # Example usage
# file_path = 'assests/full-list-of-bad-words_comma-separated-text-file_2022_05_05/full-list-of-bad-words_comma-separated-text-file_2022_05_05.txt'
# data = read_data_from_file(file_path)
# preprocessed_data = data_preprocessing(data)

# # Write preprocessed data back to the same file
# write_data_to_file(file_path, preprocessed_data)

# print("Data preprocessing and writing to file completed.")


# data = word_tokenize(data)

# import csv 
# import re 
# def load_keywords(file_path):
#     keyword = [] 
#     with open(file_path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             row = row
#             keyword.extend(row)
#     return keyword
# print(load_keywords('assests/English.csv'))


# data = '''4tube
# 8teenxxx
# alotporn
# amateurscentral
# asianscentral
# beeg
# bustnow
# cliphunter
# definebabes
# deviantclip
# drtuber
# empflix
# fantasti.cc
# fapdu
# freeporn
# freudbox
# fuq
# fux
# grayvee
# hellxx
# hustlertube
# jugy
# jizzhut
# kaktuz
# keezmovies
# kinxxx
# laraporn
# leakedporn
# lovelyclips
# lubetube
# mofosex
# monstertube
# madthumbs
# moviefap
# moviesand
# orgasm
# perfectgirls.net
# pichunter
# planetsuzy
# porn
# pornolandia
# porn-plus
# porncor
# pornhub
# pornrabbit
# porntitan
# pussy.org
# redtube
# tube8
# xhamster
# xnxx 
# xvideos
# youjizz
# '''
# from nltk.tokenize import word_tokenize
# print(word_tokenize(data))
# import re
# from config import block_words
# def nsfw(url):
#     if any(re.search(keyword, url, re.IGNORECASE) for keyword in block_words):
#         return True
#     else:
#         return False
# print(nsfw('google.com'))
# import requests
# from newspaper import Article, ArticleException
# def scrapable(url):
#     # Send a GET request to the URL
#     response = requests.get(url)

#     # Check if the request was successful (status code 200)
#     if response.status_code != 200:

#         return False

#     article = Article(url)

#     article.download()
#     try:
#         article.parse()
#     except ArticleException as e:
#         return False

#     # Access the article content
#     article_text = article.text
#     if len(article_text)==0:
#         print("False")
#         return False
#     return True

# print(scrapable('https://www.notion.so/static-check-7d22d41bd658421688a6b589a8f18750'))

# from config import check_word
# print(check_word)