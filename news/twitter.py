from django.conf import settings
from tweepy import Client


def send_tweet(text):
    API_KEY = settings.API_KEY
    API_KEY_SECRET = settings.API_KEY_SECRET
    BEARER_TOKEN = settings.BEARER_TOKEN
    ACCESS_TOKEN = settings.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

    api = Client(bearer_token=BEARER_TOKEN,
                    access_token=ACCESS_TOKEN,
                    access_token_secret=ACCESS_TOKEN_SECRET,
                    consumer_key=API_KEY,
                    consumer_secret=API_KEY_SECRET)

    api.create_tweet(text=text)
