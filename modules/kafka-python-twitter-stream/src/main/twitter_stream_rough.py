import tweepy
import json
from kafka import KafkaProducer, KafkaConsumer

CONSUMER_TWITTER_API_KEY = "jbwUhBRgkFJfnhGscTLx7AV32"
CONSUMER_TWITTER_API_KEY_SECRET = "aLQWJshji0M4IcOYCGD58tf5NWS2IarWyFGsh1BQ17fJdI8rSN"

ACCESS_TOKEN = "2603128722-PIlOFNY0cpsherRqhmeReP2tHCUTghIXzlZxp7q"
ACCESS_TOKEN_SECRET = "Ee2T27jqnLJg6JCAio4RVu1M4h5Bym4S2tac2LAoImRD5"

KAKFKA_BOOTSTRAP_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'first_hello_world_kafka_topic'

def get_auth_configure_twitter_setup():
    # create auth object (AuthN)
    auth = tweepy.OAuthHandler(CONSUMER_TWITTER_API_KEY, CONSUMER_TWITTER_API_KEY_SECRET)
    # setting access_token for (AuthZ)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return auth

# from datetime import datetime
FORMAT = "%Y-%m-%d %H:%M:%S"
def normalise_timestamp(date_time):
    return date_time.strftime(FORMAT)

def main():
    auth = get_auth_configure_twitter_setup()
    """
        Setting wait_on_rate_limit and wait_on_rate_limit_notify to True 
        makes the API object print a message and wait if the rate limit is 
        exceeded:
    """
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    twitter_search_res = api.search_tweets("IPLMediaRights")
    
    producer = KafkaProducer(bootstrap_servers=KAKFKA_BOOTSTRAP_SERVER)
    for tweet in twitter_search_res:
        
        record = f"{str(tweet.user.id_str)}; {normalise_timestamp(tweet.created_at)}; {tweet.user.followers_count}; {tweet.user.location}; {tweet.favorite_count}; {tweet.retweet_count};" 
        producer.send(KAFKA_TOPIC, str.encode(record))
        # print(record)

    consumer = KafkaConsumer(KAFKA_TOPIC, 
    bootstrap_servers=KAKFKA_BOOTSTRAP_SERVER,
    auto_offset_reset = 'earliest'
    )
    for record in consumer:
        print(record.value)
        # print(json.loads(record.value))

if __name__ == "__main__":
    main()