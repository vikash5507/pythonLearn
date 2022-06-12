# tweepy-bots/bots/config.py
import tweepy
import logging
import os


CONSUMER_TWITTER_API_KEY = "jbwUhBRgkFJfnhGscTLx7AV32"
CONSUMER_TWITTER_API_KEY_SECRET = "aLQWJshji0M4IcOYCGD58tf5NWS2IarWyFGsh1BQ17fJdI8rSN"

ACCESS_TOKEN = "2603128722-PIlOFNY0cpsherRqhmeReP2tHCUTghIXzlZxp7q"
ACCESS_TOKEN_SECRET = "Ee2T27jqnLJg6JCAio4RVu1M4h5Bym4S2tac2LAoImRD5"

KAKFKA_BOOTSTRAP_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'first_hello_world_kafka_topic'

logger = logging.getLogger()

def create_twitter_api():
    consumer_key = os.getenv("CONSUMER_TWITTER_API_KEY") or CONSUMER_TWITTER_API_KEY
    consumer_secret = os.getenv("CONSUMER_TWITTER_API_KEY_SECRET") or CONSUMER_TWITTER_API_KEY_SECRET
    access_token = os.getenv("ACCESS_TOKEN") or ACCESS_TOKEN
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET") or ACCESS_TOKEN_SECRET

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
