import creds
import tweepy
"""
check requirements.txt for environment packages
testing twitter streaming api with tweepy
"""

# * Specify file, where credentials are saved and initialize a dics with these
creds_file = "credentials.txt"
creds = creds.get_creds(creds_file)
print(creds.get("api_key"), " " ,creds.get("api_secret"))
print(creds.get("access_token"), " " ,creds.get("access_secret"))


auth = tweepy.OAuthHandler(creds.get("api_key"), creds.get("api_secret"))
auth.set_access_token(creds.get("access_token"), creds.get("access_secret"))
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
    def on_error(self, status_code):
        if status_code == 420:
            return False

stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=["python"],languages=['en'])


