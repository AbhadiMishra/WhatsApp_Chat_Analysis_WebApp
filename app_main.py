import re
import numpy as np
import pandas as pd
import emoji
import streamlit as st
import collections
from collections import Counter

st.markdown(
    "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css'>",
    unsafe_allow_html=True,
)


# Function to extract date and time
def date_time(s):
    pattern = (
        r"^([0-9]+)(\/)([0-9]+)(\/)([0-9]+), ([0-9]+):([0-9]+)([ ]|.)?(AM|PM|am|pm)? -"
    )
    result = re.match(pattern, s)
    if result:
        return True
    return False


# Function to extract author
def messenger(s):
    s = s.split(":")
    if len(s) == 2:
        return True
    else:
        return False


# Function to extract message data
def message_data(line):
    splitline = line.split(" - ")
    dateTime = splitline[0]
    date, time = dateTime.split(", ")
    message = " ".join(splitline[1:])
    if messenger(message):
        splitmessage = message.split(": ")
        author = splitmessage[0]
        message = " ".join(splitmessage[1:])
    else:
        author = None
    return date, time, author, message


# Streamlit app
def main():
    flow = st.sidebar.radio("Menu", ["Home", "Chat Analysis", "Sentiment Analysis"])

    if flow == "Home":
        home, desc = st.tabs(["Home", "Description"])
        with home:
            st.markdown(
                "<div style='position: relative;'><h1 style='color:#32CD32;'><i class='fab fa-whatsapp style='font-size: 48px;''></i> WhatsApp Chat Analysis</h1></div>",
                unsafe_allow_html=True,
            )

            st.markdown(
                """<div style='position: relative;'><h4 style=' color:#90EE90;'><i class='fa-solid fa-user-group style='font-size:22px;'></i> 
                    Group Info: <br><br> <ul style="color: #90EE90;font-family:monospace"><li> Abhinav Mishra <br><li> Avaneesh Singh</ol></h4></div>""",
                unsafe_allow_html=True,
            )
            st.markdown(
                '<hr style="border-width:1px;color:DarkSlateBlue; background-color:#F0E68C ;border:none; height:4px">',
                unsafe_allow_html=True,
            )

        with desc:
            st.markdown(
                """<h5 style="font-size:20; color:#CD853F;font-family:monospace"><u>Brief Description:</u></h5>
            <p style="font-size:18; color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
            Analyzing WhatsApp chat data can provide valuable insights beyond sentiment analysis. Here are some additional ways in which WhatsApp chat analysis can be important:
            <ul style="color:#E0FFFF;font-family:monospace"><li>Content understanding,</li>
            <li>User activity,</li>
            <li>Participant engagement,</li>
            <li>Social Network,</li>
            <li>Content and Link sharing,</li> 
            <li>User Behaviour pattern etc.</li></ul></p>
            <p style="font-size:18; font-weight:600;color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
            WhatsApp chat analysis involves studying chat data to gain insights into topics, user behavior, content sharing, engagement, and communication patterns. 
            It offers valuable information for understanding conversations, optimizing communication strategies, monitoring user activity, and more, 
            without focusing on sentiment analysis.</p>""",
                unsafe_allow_html=True,
            )

            st.markdown(
                """<table border="1" style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th colspan="2" style="text-align: center; background-color: #f2f2f2; padding: 10px;">Project Initiation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2" align="center" style="background-color: #e6f7ff; padding: 10px;">Part I: WhatsApp Chat Analysis</td>
    </tr>
    <tr>
      <td style="vertical-align: top;">
        <b>1. Data Collection</b>
      </td>
      <td style="vertical-align: top;">
        <b>2. Preprocessing</b>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;">
        <ul>
          <li>Objective Refinement and Literature Review</li>
          <li>Dataset Acquisition</li>
          <li>Data Pre-processing</li>
          <li>Technological Integration</li>
          <li>Emoji Handling</li>
        </ul>
      </td>
      <td style="vertical-align: top;">
        <ul>
          <li>Message Statistics and NLP</li>
          <li>Emoji Analysis and NLP</li>
          <li>Interactive Visualization and NLP</li>
          <li>Interdisciplinary Insights</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2" align="center" style="background-color: #e6f7ff; padding: 10px;">Part II: Sentiment Classification</td>
    </tr>
    <tr>
      <td style="vertical-align: top;">
        <b>1. Data Collection</b>
      </td>
      <td style="vertical-align: top;">
        <b>2. Preprocessing</b>
      </td>
    </tr>
    <tr>
      <td style="vertical-align: top;">
        <ul>
          <li>Dataset Overview</li>
          <li>Data Cleaning</li>
          <li>Feature Extraction</li>
        </ul>
      </td>
      <td style="vertical-align: top;">
        <ul>
          <li>Model Selection</li>
          <li>Training</li>
          <li>Visualization</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="background-color: #e6f7ff; padding: 10px;">
        <b>3. Classification and Analysis</b>
      </td>
    </tr>
    <tr>
      <td colspan="2" style="vertical-align: top;">
        <ul>
          <li>Making Predictions</li>
          <li>Evaluation Metrics</li>
          <li>Analysis</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>
""",
                unsafe_allow_html=True,
            )

    if flow == "Chat Analysis":
        # Initialize session state to keep track of visited pages
        if "visited_pages" not in st.session_state:
            st.session_state.visited_pages = set()

        page2, page3, page4, page5, page6, page8 = st.tabs(
            [
                "Upload File",
                "View Chat",
                "View Statistics",
                "Process Chat",
                "Chat Insights",
                "Interactive Plots",
            ]
        )

        with page2:
            st.markdown(
                """<h1 style="font-size:20; color:#F0E68C ;font-family:monospace"><u>Upload chat file (.txt)</u></h1>""",
                unsafe_allow_html=True,
            )
            st.markdown(
                """<h4 style="font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace">Steps to export chat from WhatsApp Application: </h4><br>
            <ol style="font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace"><li>Open Chat.</li>
            <li>Tap More options > More > Export chat.</li><li>Tap Without media.</li></ol>""",
                unsafe_allow_html=True,
            )
            if "Upload File" not in st.session_state.visited_pages:
                uploaded_file = st.file_uploader("", type=["txt"])
                if uploaded_file is not None:
                    lines = uploaded_file.readlines()
                    data = []
                    messageBuffer = []
                    date, time, author = None, None, None
                    for line in lines:
                        line = line.decode("utf-8").strip()
                        if date_time(line):
                            if len(messageBuffer) > 0:
                                data.append(
                                    [date, time, author, " ".join(messageBuffer)]
                                )
                            messageBuffer.clear()
                            date, time, author, message = message_data(line)
                            messageBuffer.append(message)
                        else:
                            messageBuffer.append(line)

                    df = pd.DataFrame(
                        data, columns=["Date", "Time", "Author", "Message"]
                    )
                    new_df = pd.DataFrame(
                        data, columns=["Date", "Time", "Author", "Message"]
                    )
                    df = df.dropna()

                    authors = df["Author"].unique()
                    author_mapping = {
                        author: f"Sender {i+1}" for i, author in enumerate(authors)
                    }
                    df["Author"].replace(author_mapping, inplace=True)
                    st.session_state.df = df
                    st.session_state.new_df = new_df
                    st.session_state.visited_pages = set()

        # View DataFrame
        with page3:
            if "View DataFrame" not in st.session_state.visited_pages:
                if "df" in st.session_state:
                    st.markdown(
                        "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Viewing Chat content as DataFrame: </h4><br>",
                        unsafe_allow_html=True,
                    )
                    with st.echo():
                        st.dataframe(st.session_state.df, width=800, height=600)
                else:
                    st.warning("Please upload the chat file, before proceeding.")

        # View Statistics
        with page4:
            if "View Statistics" not in st.session_state.visited_pages:
                if "df" in st.session_state:
                    st.markdown(
                        "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Viewing DataFrame Stats:</h4><br>",
                        unsafe_allow_html=True,
                    )
                    with st.echo():
                        st.table(st.session_state.df.describe())
                    st.markdown(
                        """
                <h5 style="font-size:20; color:#E0FFFF;font-family:monospace"><u>Overview of the above description:</u></h5>
                <p style="font-size:18; color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
                The df.describe() function in pandas is like a summary report for your data. It gives you a quick overview of the main statistics for each column (or feature) in your DataFrame. Here's what it tells you:
                <ol style="color: #E0FFFF;font-family:monospace">
                    <li><b>Count</b>: The number of non-missing (non-null) values in each column. This tells you how many data points you have for each feature.</li>
                    <li><b>Mean</b>: The average value for each feature. It's the sum of all values divided by the count. This gives you an idea of the central tendency of your data.</li>
                    <li><b>Standard Deviation (std)</b>: This measures the amount of variation or dispersion in your data. A higher standard deviation means that the data points are more spread out from the mean.</li>
                    <li><b>Minimum (min)</b>: The smallest value in each column, showing the minimum value observed.</li> 
                    <li><b>25th Percentile (25%)</b>: This is the value below which 25% of your data falls. It gives you an idea of the lower end of your data distribution.</li>
                    <li><b>50th Percentile (50%)</b>: Also known as the median, this is the value below which 50% of your data falls. It's a good measure of the central point of your data distribution.</li>
                    <li><b>75th Percentile (75%)</b>: This is the value below which 75% of your data falls. It gives you an idea of the upper end of your data distribution.</li>
                    <li><b>Maximum (max)</b>: The largest value in each column, showing the maximum value observed.</li>
                </ol></p>
                <p style="font-size:18; font-weight:600;color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
                By running df.describe(), we can quickly get a sense of the data's distribution, identify potential outliers, and understand the basic statistics of each feature in your DataFrame. It's a helpful starting point for data exploration and analysis in pandas.
                </p>""",
                        unsafe_allow_html=True,
                    )
                else:
                    st.warning("Please upload the chat file, before proceeding.")
        # Process Chat
        with page5:
            if "Process Chat" not in st.session_state.visited_pages:
                if "df" in st.session_state:
                    import time

                    with st.spinner("Loading..."):
                        time.sleep(1)
                    st.subheader("Processing Chat Data")

                    df = st.session_state.df
                    df.reset_index(drop=True, inplace=True)
                    import time

                    # Define the progress bar
                    progress_bar = st.progress(0)

                    # Define the background task
                    for i in range(95):
                        # Update the progress bar every 0.1 seconds
                        time.sleep(0.05)
                        progress_bar.progress(i + 1)

                    st.warning(
                        "Please wait - Do not switch pages, Until process completes/terminated."
                    )

                    # removing hinglish & english stopwords
                    def remove_stop_words(message):
                        f = open("stop_hinglish.txt", "r", encoding="utf-8")
                        stop_words = f.read().split()
                        return " ".join(
                            [
                                word
                                for word in message.lower().split()
                                if word not in stop_words
                            ]
                        )

                    df["Message"] = df["Message"].apply(remove_stop_words)

                    # removing punctuations
                    def remove_punctuation(message):
                        import string

                        x = re.sub("[%s]" % re.escape(string.punctuation), "", message)
                        return x

                    df["Message"] = df["Message"].apply(remove_punctuation)

                    df = df[
                        ~df["Message"].isin(
                            [
                                "This message was deleted",
                                "null",
                                "message deleted",
                                "deleted message",
                                "missed voice call",
                                "missed video call",
                                "",
                            ]
                        )
                    ]

                    df["Date&Time"] = df["Date"] + " " + df["Time"]
                    df = df.drop(["Time", "Date"], axis=1)
                    df = df[["Date&Time", "Author", "Message"]]
                    df["Date&Time"] = pd.to_datetime(
                        df["Date&Time"], dayfirst=True, format="mixed"
                    )
                    df["Only_date"] = df["Date&Time"].dt.date
                    df["Year"] = df["Date&Time"].dt.year
                    df["Month_No"] = df["Date&Time"].dt.month
                    df["Month"] = df["Date&Time"].dt.month_name()
                    df["Day"] = df["Date&Time"].dt.day
                    df["Day_name"] = df["Date&Time"].dt.day_name()
                    df["Hour"] = df["Date&Time"].dt.hour
                    df["Minute"] = df["Date&Time"].dt.minute
                    # adding hour-to-hour period
                    period = []
                    for hour in df[["Day_name", "Hour"]]["Hour"]:
                        if hour == 23:
                            period.append(str(hour) + "-" + str("00"))
                        elif hour == 0:
                            period.append(str("00") + "-" + str(hour + 1))
                        else:
                            period.append(str(hour) + "-" + str(hour + 1))
                    df["Hour_Period"] = period
                    st.session_state.df = df
                    progress_bar.empty()
                    st.warning(
                        "Process complete. Do navigate to <View Chat> page on sidebar."
                    )
                    st.session_state.visited_pages.add("Process Chat")
                else:
                    st.warning("Please upload the chat file, before proceeding.")
            else:
                st.warning(
                    "You have already processed the chat data. Do navigate to <View Chat> page on sidebar."
                )

        # Chat Insights
        with page6:

            @st.cache_data
            def chat_in():
                if "df" in st.session_state:
                    df = st.session_state.df
                    st.markdown(
                        "<h5 style='font-size:20; color:#E0FFFF;font-family:monospace'><u>Chat Insights:</u></h5><br>",
                        unsafe_allow_html=True,
                    )

                    def count_message_by_sender():
                        st.write("1. Message Count of each sender in the chat:")
                        st.dataframe(
                            st.session_state.df["Author"].value_counts().head()
                        )

                    def percentage_message_by_sender():
                        st.write(
                            "2. Percentage of message each sender sent in the chat:"
                        )
                        st.dataframe(
                            round(
                                (
                                    (
                                        st.session_state.df["Author"].value_counts()
                                        / st.session_state.df.shape[0]
                                    )
                                    * 100
                                ),
                                2,
                            )
                            .reset_index()
                            .rename(columns={"Author": "Code_Name", "count": "Percent"})
                        )

                    def word_count():
                        st.write("3. Total number of words present in the chat: ")
                        words = []
                        for message in df["Message"]:
                            words.extend(message.split())
                        st.text(len(words))

                    def media_count(df):
                        st.write("4. Total number of media files present in the chat: ")
                        df["Word_Count"] = df["Message"].str.count("media omitted")
                        WordCount = (df["Word_Count"] == 1).sum()
                        st.text(WordCount)

                    def url_count():
                        st.write(
                            "5. Total number of link(s)/url(s) present in the chat: "
                        )
                        from urlextract import URLExtract

                        extract = URLExtract()
                        links = []
                        for message in df["Message"]:
                            links.extend(extract.find_urls(message))
                        st.text(len(links))

                    def count_emoji():

                        # from collections import Counter

                        st.write("6. Top emoji(s) used in the chat: ")

                        emojis = []
                        for message in df["Message"]:
                            emojis.extend([c for c in message if c in emoji.EMOJI_DATA])
                            pd.DataFrame(
                                Counter(emojis).most_common(len(Counter(emojis)))
                            )
                        emoji_count = {}
                        for e in emojis:
                            if e in emoji_count:
                                emoji_count[e] += 1
                            else:
                                emoji_count[e] = 1
                        emoji_count = dict(
                            sorted(
                                emoji_count.items(),
                                key=lambda item: item[1],
                                reverse=True,
                            )
                        )
                        st.dataframe((dict(list(emoji_count.items())[:10])))

                    def counting_emojis():
                        st.write("7. Emoji_count by sender: ")
                        df["Emoji_Count"] = df["Message"].str.count(
                            r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FAB0-\U0001FABF\U0001FAC0-\U0001FAFF\U0001FAD0-\U0001FAFF\U0001FAE0-\U0001FAFF\U0001FAF0-\U0001FAFF\U0001F4AA]"
                        )
                        emoji_counts = (
                            df.groupby("Author")["Emoji_Count"]
                            .sum()
                            .sort_values(ascending=False)
                        )
                        st.write(emoji_counts[:10])

                    def wordfreq_():
                        st.write("8. Most frequent words:")

                        def rem_emojis(text):
                            return emoji.demojize(text, delimiters=(" ", " "))

                        new_df = df["Message"].apply(rem_emojis)
                        with open("abusive_main.txt", "r") as file:
                            words_to_remove = file.read().splitlines()
                        for word in words_to_remove:
                            new_df = new_df[new_df != word]
                        new_df = new_df[new_df != "media omitted"]
                        word_freq = collections.Counter(new_df)
                        st.dataframe(word_freq.most_common(20))

                    # Executing Methods:
                    count_message_by_sender()
                    percentage_message_by_sender()
                    word_count()
                    media_count(df)
                    url_count()
                    count_emoji()
                    counting_emojis()
                    wordfreq_()

                else:
                    st.warning("Please upload the chat file, before proceeding.")

            chat_in()

        with page8:

            if "df" in st.session_state:
                import matplotlib.pyplot as plt
                import seaborn as sns

                df = st.session_state.df
                st.set_option("deprecation.showPyplotGlobalUse", False)
                st.markdown(
                    "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Interactive Plots: </h4><br>",
                    unsafe_allow_html=True,
                )
                tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
                    [
                        "Daily_Timeline",
                        "Monthly_Timeline",
                        "Busiest_Day",
                        "Busiest_Month",
                        "Busiest_Hours in a day",
                        "Word_Cloud",
                    ],
                )

                with tab5:

                    def heatmap_():
                        plt.figure(figsize=(9, 10))
                        sns.heatmap(
                            df.pivot_table(
                                index="Day_name",
                                columns="Hour_Period",
                                values="Message",
                                aggfunc="count",
                            ).fillna(0)
                        )
                        plt.yticks(rotation="vertical")
                        fig = plt.show()
                        # Display the heatmap using st.pyplot()
                        st.pyplot(fig)

                    heatmap_()

                with tab4:

                    def busyMonth():

                        busy_month = df["Month"].value_counts()
                        st.bar_chart(busy_month, height=600)

                    busyMonth()

                with tab3:

                    def busyDay():

                        busy_day = df["Day_name"].value_counts()
                        st.bar_chart(busy_day, height=600)

                    busyDay()
                with tab2:

                    def monthly_():

                        monthly_timeline = (
                            df.groupby("Month").count()["Message"].reset_index()
                        )
                        st.scatter_chart(
                            monthly_timeline,
                            x="Month",
                            y="Message",
                            height=500,
                            width=200,
                        )

                    monthly_()
                with tab1:

                    def daily_():
                        daily_timeline = (
                            df.groupby("Only_date").count()["Message"].reset_index()
                        )
                        st.scatter_chart(
                            daily_timeline,
                            x="Only_date",
                            y="Message",
                            height=500,
                            width=200,
                        )

                    daily_()

                with tab6:
                    from wordcloud import WordCloud

                    def wordcloud_():
                        words = df["Message"]
                        text = " ".join(words)
                        # Create a WordCloud object with increased max_words
                        wordcloud = WordCloud(
                            width=1400,
                            height=800,
                            background_color="white",
                            max_words=20,
                        ).generate(text)

                        # Plot the WordCloud
                        plt.figure(figsize=(30, 35))
                        plt.imshow(wordcloud, interpolation="bilinear")
                        plt.axis("off")
                        fig = plt.show()
                        st.pyplot(fig)

                    wordcloud_()

            else:
                st.warning("Please upload the chat file, before proceeding.")

    elif flow == "Sentiment Analysis":
        st.markdown(
            """<h1 style="font-size:20; color:#F0E68C ;font-family:monospace"><u> Sentiment Classification</u></h1>
                <h4 style="font-size:20; color:#F0E68C ;font-family:monospace">Model: Naive Bayes Multinomial</h4>
                <h4 style="font-size:20; color:#F0E68C ;font-family:monospace">Vectorizer: TF-IDF</h4>
                <h4 style="font-size:20; color:#F0E68C ;font-family:monospace">Dump & Loaded: Joblib</h4>""",
            unsafe_allow_html=True,
        )
        if "new_df" in st.session_state:
            new_df = st.session_state.new_df

            # loading Model
            from joblib import load

            model_ = load("multinomialNB799.joblib")

            # Making Predictions
            predictions = model_.predict(new_df["Message"])

            # converting predicted values to string labels
            sentiment_labels = {-1: "negative", 0: "neutral", 1: "positive"}
            predicted_sentiments = [sentiment_labels[pred] for pred in predictions]

            # creating final Dataframe
            result_df = pd.DataFrame(
                {"Message": new_df["Message"], "Sentiment": predicted_sentiments}
            )

            # dsisplaying dataframe
            st.dataframe(result_df)

        else:
            st.warning("Please upload the chat file, before proceeding.")


if __name__ == "__main__":
    main()
