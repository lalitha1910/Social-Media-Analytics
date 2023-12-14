import pandas as pd
import numpy as np
import random

# Function to generate random dates with time
def random_dates_with_time(start, end, n=10):
    start_u = start.value//10**9
    end_u = end.value//10**9
    dates = pd.to_datetime(np.random.randint(start_u, end_u, n), unit='s')

    # Adding random times to the dates
    times = pd.to_timedelta(np.random.randint(0, 86400, n), unit='s')
    return dates + times

# Setting a seed for reproducibility
random.seed(42)
np.random.seed(42)

# Sample size
n = 1000

# Base dataset creation
data = {
    "User ID": np.random.randint(1000, 9999, n),
    "Frequency of Posts": np.random.randint(1, 30, n),
    "Post Type": np.random.choice(["Image", "No Image"], n),
    "Likes": np.random.randint(0, 500, n),
    "Comments": np.random.randint(0, 200, n),
    "Retweets": np.random.randint(0, 100, n),
    "Sentiment of Post": np.random.choice(["Positive", "Negative", "Neutral"], n),
    "Sentiment of Comments": np.random.choice(["Positive", "Negative", "Neutral"], n),
    "Date of Post": random_dates_with_time(pd.to_datetime('2023-11-01'), pd.to_datetime('2023-11-30'), n)
}
df = pd.DataFrame(data)

# Modifications as per the hypotheses
df['Number of Followers'] = df['Frequency of Posts'] * np.random.randint(50, 150, n)
image_multiplier = 1.5
df.loc[df['Post Type'] == 'Image', ['Likes', 'Comments', 'Retweets']] *= image_multiplier
negative_sentiment_multiplier = 1.8
df.loc[df['Sentiment of Post'] == 'Negative', 'Retweets'] *= negative_sentiment_multiplier

# Adding engagement column
df['Engagement'] = df['Likes'] + df['Comments'] + df['Retweets']

# Modify values for evening time (18:00 to 23:59) to have higher engagement
evening_hours = df['Date of Post'].dt.hour.between(18, 23)
df.loc[evening_hours, 'Engagement'] *= np.random.uniform(1.2, 1.5)

# Rounding 'Likes', 'Comments', 'Shares', and 'Engagement' to remove decimal values
df['Likes'] = df['Likes'].round().astype(int)
df['Comments'] = df['Comments'].round().astype(int)
df['Retweets'] = df['Retweets'].round().astype(int)
df['Engagement'] = df['Engagement'].round().astype(int)

# Save the DataFrame to a CSV file
df.to_csv('social_media_data.csv', index=False)
