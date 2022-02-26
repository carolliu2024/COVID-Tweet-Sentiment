# Script Author: Martin Beck
# Medium Article Follow-Along: https://medium.com/better-programming/how-to-scrape-tweets-with-snscrape-90124ed006af

# Pip install the command below if you don't have the development version of snscrape 
# !pip install git+https://github.com/JustAnotherArchivist/snscrape.git

# Run the below command if you don't already have Pandas
# !pip install pandas

# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Below are two ways of scraping using the Python Wrapper.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
# Setting variables to be used below
# maxTweets = 100

# Creating list to append tweet data to
# tweets_list1 = []

# Using TwitterSearchScraper to scrape data 
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:jack').get_items()):
#     if i>maxTweets:
#         break
#     tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
# tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into a CSV
# tweets_df1.to_csv('user-tweets.csv', sep=',', index=False)


# Query by text search
# Setting variables to be used below

# CREATE COVID CSV FILE
# Creating list to append tweet data to
covid_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid OR covid-19 OR covid 19 OR corona OR coronavirus OR virus since:2022-02-18 until:2022-02-19').get_items()):
    if i > 100:
        break
    covid_list.append([tweet.date, tweet.user.location, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.replyCount])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(covid_list, columns=['Datetime', 'Location', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Retweet Count', 'Reply Count'])

# Display first 5 entries from dataframe
# tweets_df.head()

# Export dataframe into a CSV
tweets_df.to_csv('covid-tweets.csv', sep=',', index=False)


# -------------------------------------------------------
# CREATE MASK MANDATE CSV FILE
# Creating list to append tweet data to
# mask_list = []

# # Using TwitterSearchScraper to scrape data and append tweets to list
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mask OR masks OR mask mandate OR face mask OR facemask OR facemasks since:2022-02-18 until:2022-02-19').get_items()):
#     if i > 10000:
#         break
#     mask_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.replyCount])

# # Creating a dataframe from the tweets list above
# tweets_df1 = pd.DataFrame(mask_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Retweet Count', 'Reply Count'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into a CSV
# tweets_df1.to_csv('mask-tweets.csv', sep=',', index=False)


# -------------------------------------------------------
# CREATE VACCINE CSV FILE
# Creating list to append tweet data to
# vaccine_list = []

# # Using TwitterSearchScraper to scrape data and append tweets to list
# for i,tweet in enumerate(sntwitter.TwitterSearchScraper('vaccine OR vaccinated OR vaxxed OR vaccines OR booster shot since:2022-02-18 until:2022-02-19').get_items()):
#     if i > 500:
#         break
#     vaccine_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.likeCount, tweet.retweetCount, tweet.replyCount])

# # Creating a dataframe from the tweets list above
# tweets_df2 = pd.DataFrame(vaccine_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username', 'Like Count', 'Retweet Count', 'Reply Count'])

# # Display first 5 entries from dataframe
# # tweets_df.head()

# # Export dataframe into a CSV
# tweets_df2.to_csv('vaccine-tweets.csv', sep=',', index=False)
