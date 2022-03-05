import pandas as pd
from sqlalchemy import all_
import text2emotion as te
import csv


#Covid Tweets CSV
data= pd.read_csv(r"C:\Users\alexa\OneDrive\Desktop\covid-tweets1.csv")
sum_happy = 0
sum_angry = 0
sum_surprise = 0
sum_sad= 0
sum_fear = 0
count = 0

sum_happy_weighted = 0
sum_angry_weighted = 0
sum_surprise_weighted = 0
sum_sad_weighted= 0
sum_fear_weighted = 0
current_row =0
total_likes = 0

for row in data.Text:
    all_emotions_values = te.get_emotion(row)
    if all_emotions_values['Happy'] != 0 or all_emotions_values['Angry'] !=0 or all_emotions_values['Surprise'] != 0 or all_emotions_values['Sad'] != 0 or all_emotions_values['Fear'] != 0 :
        sum_happy += all_emotions_values['Happy']
        sum_angry += all_emotions_values['Angry']
        sum_surprise += all_emotions_values['Surprise']
        sum_sad += all_emotions_values['Sad']
        sum_fear += all_emotions_values['Fear']
        sum_happy_weighted += (all_emotions_values['Happy'] * (data.Like_Count[current_row] + 1))
        sum_angry_weighted += (all_emotions_values['Angry'] * (data.Like_Count[current_row] + 1))
        sum_surprise_weighted += (all_emotions_values['Surprise'] * (data.Like_Count[current_row]+1))
        sum_sad_weighted += (all_emotions_values['Sad'] * (data.Like_Count[current_row]+1))
        sum_fear_weighted += (all_emotions_values['Fear'] * (data.Like_Count[current_row]+1))
        total_likes += (data.Like_Count[current_row] + 1)
        count = count + 1
    current_row += 1
results = {'Happy': round(sum_happy/count,2), 'Angry': round(sum_angry/count,2), 'Surprise': round(sum_surprise/count,2), 'Sad': round(sum_sad/count,2), 'Fear': round(sum_fear/count,2)}
print("Results for Unweighted Covid-Tweets: " + str(results))

results1 = {'Happy': round(sum_happy_weighted/total_likes,2), 'Angry': round(sum_angry_weighted/total_likes,2), 'Surprise': round(sum_surprise_weighted/total_likes,2), 'Sad': round(sum_sad_weighted/total_likes,2), 'Fear': round(sum_fear_weighted/total_likes,2)}
print("Results for Weighted Covid-Tweets: " + str(results1))

#Finds the Top Tweet
top_tweet_likes = 0
top_tweet_text = 0
top_tweet_row = 0
current_row = 0
username = "hi"
for row in data.Like_Count:
    if row>=top_tweet_likes:
        top_tweet_likes = row
        top_tweet_row = current_row
        top_tweet_text = data.Text[current_row]
        username = data.Username[current_row]
    current_row += 1
print("The top tweet is by " + username + " and has " + str(top_tweet_likes) + " likes: " + top_tweet_text)


#vaccine-tweets
data= pd.read_csv(r"C:\Users\alexa\OneDrive\Desktop\vaccine-tweets.csv")
sum_happy = 0
sum_angry = 0
sum_surprise = 0
sum_sad= 0
sum_fear = 0
count = 0

sum_happy_weighted = 0
sum_angry_weighted = 0
sum_surprise_weighted = 0
sum_sad_weighted= 0
sum_fear_weighted = 0
current_row =0
total_likes = 0

for row in data.Text:
    all_emotions_values = te.get_emotion(row)
    if all_emotions_values['Happy'] != 0 or all_emotions_values['Angry'] !=0 or all_emotions_values['Surprise'] != 0 or all_emotions_values['Sad'] != 0 or all_emotions_values['Fear'] != 0 :
        sum_happy += all_emotions_values['Happy']
        sum_angry += all_emotions_values['Angry']
        sum_surprise += all_emotions_values['Surprise']
        sum_sad += all_emotions_values['Sad']
        sum_fear += all_emotions_values['Fear']
        sum_happy_weighted += (all_emotions_values['Happy'] * (data.Like_Count[current_row] + 1))
        sum_angry_weighted += (all_emotions_values['Angry'] * (data.Like_Count[current_row] + 1))
        sum_surprise_weighted += (all_emotions_values['Surprise'] * (data.Like_Count[current_row]+1))
        sum_sad_weighted += (all_emotions_values['Sad'] * (data.Like_Count[current_row]+1))
        sum_fear_weighted += (all_emotions_values['Fear'] * (data.Like_Count[current_row]+1))
        total_likes += (data.Like_Count[current_row] + 1)
        count = count + 1
    current_row += 1
results = {'Happy': round(sum_happy/count,2), 'Angry': round(sum_angry/count,2), 'Surprise': round(sum_surprise/count,2), 'Sad': round(sum_sad/count,2), 'Fear': round(sum_fear/count,2)}
print("Results for Unweighted Covid-Tweets: " + str(results))

results1 = {'Happy': round(sum_happy_weighted/total_likes,2), 'Angry': round(sum_angry_weighted/total_likes,2), 'Surprise': round(sum_surprise_weighted/total_likes,2), 'Sad': round(sum_sad_weighted/total_likes,2), 'Fear': round(sum_fear_weighted/total_likes,2)}
print("Results for Weighted Covid-Tweets: " + str(results1))

#Finds the Top Tweet
top_tweet_likes = 0
top_tweet_text = 0
top_tweet_row = 0
current_row = 0
username = "hi"
for row in data.Like_Count:
    if row>=top_tweet_likes:
        top_tweet_likes = row
        top_tweet_row = current_row
        top_tweet_text = data.Text[current_row]
        username = data.Username[current_row]
    current_row += 1
print("The top tweet is by " + username + " and has " + str(top_tweet_likes) + " likes: " + top_tweet_text)

#mask-tweets
data= pd.read_csv(r"C:\Users\alexa\OneDrive\Desktop\mask-tweets.csv")
sum_happy = 0
sum_angry = 0
sum_surprise = 0
sum_sad= 0
sum_fear = 0
count = 0

sum_happy_weighted = 0
sum_angry_weighted = 0
sum_surprise_weighted = 0
sum_sad_weighted= 0
sum_fear_weighted = 0
current_row =0
total_likes = 0

for row in data.Text:
    all_emotions_values = te.get_emotion(row)
    if all_emotions_values['Happy'] != 0 or all_emotions_values['Angry'] !=0 or all_emotions_values['Surprise'] != 0 or all_emotions_values['Sad'] != 0 or all_emotions_values['Fear'] != 0 :
        sum_happy += all_emotions_values['Happy']
        sum_angry += all_emotions_values['Angry']
        sum_surprise += all_emotions_values['Surprise']
        sum_sad += all_emotions_values['Sad']
        sum_fear += all_emotions_values['Fear']
        sum_happy_weighted += (all_emotions_values['Happy'] * (data.Like_Count[current_row] + 1))
        sum_angry_weighted += (all_emotions_values['Angry'] * (data.Like_Count[current_row] + 1))
        sum_surprise_weighted += (all_emotions_values['Surprise'] * (data.Like_Count[current_row]+1))
        sum_sad_weighted += (all_emotions_values['Sad'] * (data.Like_Count[current_row]+1))
        sum_fear_weighted += (all_emotions_values['Fear'] * (data.Like_Count[current_row]+1))
        total_likes += (data.Like_Count[current_row] + 1)
        count = count + 1
    current_row += 1
results = {'Happy': round(sum_happy/count,2), 'Angry': round(sum_angry/count,2), 'Surprise': round(sum_surprise/count,2), 'Sad': round(sum_sad/count,2), 'Fear': round(sum_fear/count,2)}
print("Results for Unweighted Covid-Tweets: " + str(results))

results1 = {'Happy': round(sum_happy_weighted/total_likes,2), 'Angry': round(sum_angry_weighted/total_likes,2), 'Surprise': round(sum_surprise_weighted/total_likes,2), 'Sad': round(sum_sad_weighted/total_likes,2), 'Fear': round(sum_fear_weighted/total_likes,2)}
print("Results for Weighted Covid-Tweets: " + str(results1))

#Finds the Top Tweet
top_tweet_likes = 0
top_tweet_text = 0
top_tweet_row = 0
current_row = 0
username = "hi"
for row in data.Like_Count:
    if row>=top_tweet_likes:
        top_tweet_likes = row
        top_tweet_row = current_row
        top_tweet_text = data.Text[current_row]
        username = data.Username[current_row]
    current_row += 1
print("The top tweet is by " + username + " and has " + str(top_tweet_likes) + " likes: " + top_tweet_text)


