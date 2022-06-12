import tweepy
import json, time
from typing import List, Dict
from kafka import KafkaProducer
from config import create_twitter_api, KAKFKA_BOOTSTRAP_SERVER, KAFKA_TOPIC

# from datetime import datetime
FORMAT = "%Y-%m-%d %H:%M:%S"
def normalise_timestamp(date_time):
    return date_time.strftime(FORMAT)

def serializer(message):
    return message.encode("utf-8")
    #return json.dumps(message).encode("utf-8")

producer = KafkaProducer(
    bootstrap_servers=KAKFKA_BOOTSTRAP_SERVER,
    value_serializer=serializer
)

def search_on_twitter(search_keyword: str, max_count: int = 10) -> List[Dict]:
    tweets = api.search_tweets(search_keyword, count=max_count)

    tweets_list = []
    for tweet in tweets:
        record = f"{str(tweet.user.id_str)}; {normalise_timestamp(tweet.created_at)}; {tweet.user.followers_count}; {tweet.user.location}; {tweet.favorite_count}; {tweet.retweet_count};" 
        tweets_list.append(record)
    
    return tweets_list

if __name__ == "__main__":
    api = create_twitter_api()
    # trends = api.available_trends()
    # print(trends)

    # while True:
    keyword_to_search_for = "Biharsharif"
    tweets = search_on_twitter(keyword_to_search_for)
    print(f"Before sending records by kafka producer")
    for tweet in tweets:
        # record = f"{str(tweet.user.id_str)}; {normalise_timestamp(tweet.created_at)}; {tweet.user.followers_count}; {tweet.user.location}; {tweet.favorite_count}; {tweet.retweet_count};" 
        producer.send(KAFKA_TOPIC, tweet)

    time.sleep(5)
