import creds
import oauth_tweeter
import streamLIstener
"""
check requirements.txt for environment packages
testing twitter streaming api with tweepy
"""

# * Specify file, where credentials are saved and initialize a dics with these
creds_file = "credentials.txt"
creds = creds.get_creds(creds_file)


api = oauth_tweeter.oauth(creds.get("api_key"), creds.get(
    "api_secret"), creds.get("access_token"), creds.get("access_secret"))


filter_exp = [
    'bitcoin',
    'bitcoinprice',
    'bitcoinvalue',
    'btc',
    'bitcoins',
    'bitcoinnews'
]

languages = ['en']

streamLIstener.get_stream_listener(api,filter_exp,languages)
