import tweepy
# my keys and tokens from twitter App
consumerKey = ""
consumerSecret = ""
accessToken = ""
accessTokenSecret = ""

# authentication process using keys and tokens
auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.secure = True
auth.set_access_token(accessToken,accessTokenSecret)

#API provided by twitter
api = tweepy.API(auth)

# return the user information who authenticated
profile = api.me()

# display user information form the Json response
print("Profile")
print("name is " + profile.name) # my name
print("Username is " + profile.screen_name) # my twitter username
print("location is " + profile.location) # my location on twitter
print("bio is " + profile.description) # my bio
print("followers count" , profile.followers_count) # the number of followers I have
print("following count" , profile.friends_count) # the number of account I follow
print("")

print("timeline")
#returns 20 tweets from your twitter homepage(timeline) from you and who you follow
tweets = api.home_timeline()

for tweet in tweets:
    print("name: " + tweet.user.name) # The twitter handle of the tweeter
    print("tweet: " + tweet.text) # the actual tweet text
    print("favourites:" , tweet.favorite_count) # The number of likes of the tweet
    print("retweets:" , tweet.retweet_count) # The number of ReTweets of the tweet
    print("")
print("")

print("followers")
# returns the last 20 people users who followed me
followers = api.followers()

for follower in followers:
    print("username: " +follower.screen_name) # Twitter handle of the the follower
    print("name: " +follower.name) # Name of the follower
    print("")
print("")

print("following")
#gets the last 20 people I followed as a list
friends = api.friends()

for friend in friends:
    print("username: " +friend.screen_name) # Twitter handle of the friend
    print("name: " +friend.name) # name of friend
    print("")
