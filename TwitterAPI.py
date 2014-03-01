import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'QEN0pRUDWBwz3eAnRGt4oA'
consumer_secret = 'uPKpmdkUyEtHHYTG81hxrDe2kPybRZq8zfAnAvdrA'
access_token = '109282672-lsdLzFwO2ybQ8f00qZG51JTcel7zTghEBa00R24c'
access_token_secret = 'TE717i4SK6uuHUBmak8UXLaUijNH2uV1H5HbrCSnG5c'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status('#savethehacker venue is cool to work')

user =api.me()
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))




