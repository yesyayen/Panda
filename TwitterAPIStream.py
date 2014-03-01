import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'QEN0pRUDWBwz3eAnRGt4oA'
consumer_secret = 'uPKpmdkUyEtHHYTG81hxrDe2kPybRZq8zfAnAvdrA'
access_token = '109282672-lsdLzFwO2ybQ8f00qZG51JTcel7zTghEBa00R24c'
access_token_secret = 'TE717i4SK6uuHUBmak8UXLaUijNH2uV1H5HbrCSnG5c'

class TwitterAPIStream(StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, status):
        # Prints the text of the tweet
        print('Tweet text: ' + status.text)

        # There are many options in the status object,
        # hashtags can be very easily accessed.
        for hashtag in status.entries['hashtags']:
            print(hashtag['text'])

    return true

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, listener)
    stream.filter(follow=[38744894], track=['#pythoncentral'])
