import requests

from transformers import pipeline

API_KEY = open('API_KEY').read()

keyword = 'Apple'
date = '2025-12-01'
language = 'en'

pipe = pipeline("text-classification", model="ProsusAI/finbert")

url = (
    'https://newsapi.org/v2/everything?'
    f'q={keyword}&'
    f'from={date}&'
    f'language={language}&'
    'sortBy=popularity&'
    f'apiKey={API_KEY}'
)
responses = requests.get(url)
articles = responses.json()['articles']
articles = [article for article in articles if keyword.lower() in article['title'].lower() or keyword.lower() in article['description'].lower()]

total_score= 0
num_articles = 0

for i, article in enumerate(articles):
    if keyword.lower() not in article['title'].lower() and keyword.lower() not in article['description'].lower():
        continue

    print(f'Title: {article["title"]}')
    print(f'Link : {article["url"]}')
    print(f'Summary: {article["description"]}')
    print(f'Published: {article["publishedAt"]}')

    text = (article.get('content') or (article.get('title', '') + ' ' + article.get('description', ''))).strip()
    if not text:
        continue

    scores = pipe(text, return_all_scores=True)[0]
    score_map = {s['label'].lower(): s['score'] for s in scores}
    pos = score_map.get('positive', 0.0)
    neg = score_map.get('negative', 0.0)
    neu = score_map.get('neutral', 0.0)
    pred_label = max(score_map, key=score_map.get)
    pred_score = score_map[pred_label]
    print(f'Sentiment: {pred_label}, Score: {pred_score}, Positive: {pos}, Negative: {neg}, Neutral: {neu}')
    print('-' * 40)

    if pred_label == 'positive':
        total_score += pred_score
        pos_score += pred_score
        num_articles += 1
    elif pred_label == 'negative':
        total_score -= pred_score
        neg_score += pred_score
        num_articles += 1
    else:
        pass
if num_articles:
    final_score = total_score / num_articles
    print(f'Overall Sentiment: {"Positive" if final_score >= 0.15 else "Negative" if final_score <= -0.15 else "Neutral"}{final_score}')
else:
    print('No articles with positive/negative sentiment; all neutral or no valid text')
