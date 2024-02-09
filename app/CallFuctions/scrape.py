import re
from youtube_transcript_api import YouTubeTranscriptApi
from newspaper import Article, ArticleException
def youtube_caption(url):
    video_id_match = re.search(r'(?:youtu\.be/|youtube\.com/embed/|youtube\.com/v/|youtube\.com/watch\?v=|youtube\.com/\S*?[?&]v=|youtube\.com/\S*?embed/\S*?|youtube\.com/\S*?v=)([^"&?/ ]{11})', url)
    
    if video_id_match:
        video_id = video_id_match.group(1)
    else:
        print("Invalid YouTube URL")
        return False
    data = YouTubeTranscriptApi.get_transcript(video_id)
    text = ""
    for i in range(len(data)):
        text += data[i]['text'] + " "
    return text
def article_scrape(url):
    article = Article(url)

    article.download()
    try:
        article.parse()
    except ArticleException as e:
        print("False")
        return False

    # Access the article content
    article_text = article.text
    return article_text