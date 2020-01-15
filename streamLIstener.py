import tweepy


unwanted_expressions = [
    "giveaway",
    "rt @",
    "give away",
    "check out"

]


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status,eliminated_exp):
        if any(s in status.text.lower() for s in eliminated_exp):
            return
        # for x in unwanted_expressions:
            # if x not in status.text.lower():
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False


def get_stream_listener(api,filter_exp,languages):

    stream_listener = MyStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=filter_exp, languages=languages)
