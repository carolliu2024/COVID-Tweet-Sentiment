# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import timedelta, date, datetime
# pip uninstall snscrape
# pip install snscrape==0.4.2.20211215
# We cant use the latest version or there will be errors


def find_Tweets(state, city, radius):
    covid_list = []

    start_date = date(2020, 3, 11)
    next_date = date(2020, 3, 12)
    end_date = datetime.today() 
    delta = timedelta(days=1)
    j = 1

    while start_date <= end_date.date():
        print(start_date)

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid OR covid-19 OR covid 19 OR corona OR coronavirus OR virus since:{} until:{} near:"{}" within:{}km'.format(start_date, next_date, city, radius)).get_items()):
            try:
                covid_list.append([tweet.date, tweet.user.location,tweet.content, tweet.likeCount])
        
            except Exception:
                pass
        start_date += delta
        next_date += delta

    tweets_df = pd.DataFrame(covid_list, columns=['Datetime', 'Location', 'Text', 'Like Count'])
    # print(tweets_df)

        
    # Display first 5 entries from dataframe
    # tweets_df.head()

    # Export dataframe into a CSV
    tweets_df.to_csv(f'{state}-covid-tweets-.csv', sep=',', index=False)


    '''
    '''

# find_Tweets("Montana", "Billings", 110)
# find_Tweets("Nebraska", "Omaha", 140)
# find_Tweets("Nevada", "Las Vegas", 150)
find_Tweets("New Hampshire", "Manchester, New Hampshire", 50) 
# find_Tweets("New Jersey", "Newark", 50)
# find_Tweets("New Mexico", "Albuquerque", 200)
# find_Tweets("New York", "New York City", 170)
# find_Tweets("North Carolina", "Charlotte", 100)
# find_Tweets("North Dakota", "Fargo", 130)
# find_Tweets("Ohio", "Columbus", 125)
# find_Tweets("Oklahoma", "Oklahoma City", 140)
# find_Tweets("Oregon", "Portland", 200)
# find_Tweets("Pennsylvania", "Philadelphia", 100)
# find_Tweets("Rhode Island", "Providence", 25)
# find_Tweets("South Carolina", "Charleston", 120)
# find_Tweets("South Dakota", "Sioux Falls", 130)
# find_Tweets("Tennessee", "Nashville", 70)
# find_Tweets("Texas", "Houston", 400)
# find_Tweets("Utah", "Salt Lake City", 120)
find_Tweets("Vermont", "Burlington, Vermont", 50)

# find_Tweets("Virginia", "Virginia Beach", 120)
# find_Tweets("Washington", "Seattle", 150)
find_Tweets("West Virginia", "Charleston, West Virginia", 90)
# find_Tweets("Wisconsin", "Milwaukee", 150)
# find_Tweets("Wyoming", "Cheyenne", 120)

