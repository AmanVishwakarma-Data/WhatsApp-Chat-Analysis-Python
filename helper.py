from urlextract import URLExtract
import pandas as pd
from collections import Counter
import emoji



extractor = URLExtract()
def fetch_stats(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]
        #fetch number of messages
    num_messages =  df.shape[0]
        #number of words
    words = [word for message in df["messages"] for word in message.split()]
    # num_media_messages = df[df["messages"] == "<Media omitted>\n"].shape[0]
    num_media_messages = df[df["messages"].str.contains("Media omitted", na=False)].shape[0]
    links = [url for message in df["messages"] for url in extractor.find_urls(str(message))]
    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df["users"].value_counts().head()

    df = round((df["users"].value_counts()/df.shape[0])*100,2).reset_index().rename(columns = {"users":"name","count":"percent"})
    return x, df

def most_common_words(selected_user,df):
    with open("stop_hinglish.txt", "r") as f:
        stop_words = f.read()
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]
    temp = df[df["users"] != "group notification"]
    temp = temp[temp["messages"] != "<Media omitted>\n"]
    words = []
    for message in temp["messages"]:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    # most_common_df = pd.DataFrame(Counter(words).most_common(25))
    most_common_df = pd.DataFrame(Counter(words).most_common(25)).rename(columns={0: "words", 1: "count"})
    return most_common_df

def emoji_helper(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]
    emojies = []
    for message in df["messages"]:
        emojies.extend([c for c in message if c in emoji.EMOJI_DATA])

    emoji_df = pd.DataFrame(Counter(emojies).most_common(len(Counter(emojies))),columns=['Emoji', 'Count'])
    return emoji_df

def monthly_timeline(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]

    df["month_num"] = df["date"].dt.month
    timeline = df.groupby(["year", "month", "month_num"]).count()["messages"].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline["month"][i] + "-" + str(timeline["year"][i]))
    timeline["time"] = time

    return timeline

def daily_time_line(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]
    df["only_date"] = df["date"].dt.date
    daily_timeline = df.groupby('only_date').count()["messages"].reset_index()

    return daily_timeline

def week_activity_map(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]

    df["day_name"] = df.date.dt.day_name()
    return df["day_name"].value_counts()


def month_activity_map(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]

    return df["month"].value_counts()

def activity_heatmap(selected_user,df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]
    period = []
    for hour in df[["day_name", "hour"]]["hour"]:
        if hour == 23:
            period.append(str(hour) + "-" + str("00"))
        elif hour == 0:
            period.append(str("00") + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df["period"] = period

    user_heatmap = df.pivot_table(index="day_name",columns="period",values="messages",aggfunc="count").fillna(0)
    return user_heatmap


