import re
from time import sleep
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
    s = s.split(":", 1)
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

    # Initialize session state to keep track of visited pages

    if "visited_pages" not in st.session_state:
        st.session_state.visited_pages = set()
    page = st.sidebar.radio(
        "Menu",
        [
            "Home",
            "Upload File",
            "Process Chat",
            "View Chat",
            "Chat Insights",
            "Interactive Plots",
            "Sentiment Analysis",
        ],
    )

    if page == "Home":
        Home, Introduction, Project = st.tabs(
            ["Home", "Introduction", "Project Initialization"]
        )
        with Home:
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
        with Introduction:

            st.markdown(
                """
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WhatsApp Chat Analysis</title>
<head>
   <style>
      table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      }
      th, td {
      padding: 8px;
      text-align: left;
      border-bottom: 1px solid #ddd;
      }
      th {
      text-align: center; 
      background-color: rgb(255,255,255); 
      padding: 10px; 
      color: rgb(0,0,0);
      }
   </style>
</head>
<body>
   <h1>Analysis of WhatsApp Chats</h1>
   <p>Analyzing WhatsApp chats can serve various purposes depending on the context:</p>
   <ol>
      <li><strong>Communication Patterns:</strong> Understanding how people communicate can offer insights into their relationships, interests, and behaviors. Analyzing WhatsApp chats can reveal patterns in communication frequency, topics discussed, and preferred communication styles.</li>
      <li><strong>Sentiment Analysis:</strong> By examining the language used in WhatsApp chats, sentiment analysis can be conducted to gauge the overall mood or sentiment of the participants. This can be useful for businesses to understand customer satisfaction or for researchers studying social dynamics.</li>
      <li><strong>Social Research:</strong> WhatsApp chats can be a rich source of data for social researchers studying various aspects of human interaction, such as language evolution, cultural norms, or group dynamics.</li>
      <li><strong>Forensic Analysis:</strong> In legal contexts, WhatsApp chats may be analyzed forensically to gather evidence related to criminal activities or disputes. This can involve retrieving deleted messages, verifying the authenticity of conversations, or tracing communication patterns.</li>
      <li><strong>Behavioral Analysis:</strong> Psychologists or sociologists may analyze WhatsApp chats to understand individual or group behaviors, such as decision-making processes, social influence, or the spread of information and opinions within a network.</li>
      <li><strong>Language Study:</strong> Linguists may analyze WhatsApp chats to study language use in informal settings, including slang, emoticons, or linguistic innovations.</li>
   </ol>
   <p>Overall, analyzing WhatsApp chats can provide valuable insights into human communication, behavior, and social dynamics across various contexts.</p>
   <h3>Example Table for WhatsApp Chat Analysis:</h3>
   <table>
      <tr>
         <th style= 'background-color: #A9A9A9' >Metric</th>
         <th style= 'background-color: #A9A9A9' >Description</th>
         <th style= 'background-color: #A9A9A9' > Result</th>
      </tr>
      <tr>
         <td>Sentiment Score</td>
         <td>Analyzes the emotional tone of the chat</td>
         <td>Overall positive sentiment with occasional spikes in negativity</td>
      </tr>
      <tr>
         <td>Word Frequency</td>
         <td>Most frequently used words or phrases</td>
         <td>"Meeting", "Project", "Deadline" are frequently used words</td>
      </tr>
      <tr>
         <td>Network Analysis</td>
         <td>Mapping connections between participants</td>
         <td>Central figure identified, with subgroups forming around specific topics</td>
      </tr>
      <tr>
         <td>Peak Activity Times</td>
         <td>Identifying peak periods of message activity</td>
         <td>Most activity observed during lunch breaks and evenings</td>
      </tr>
      <tr>
         <td>Keyword Tracking</td>
         <td>Monitoring specific keywords or phrases</td>
         <td>"Sales", "Report", "Client" are trending topics</td>
      </tr>
   </table>
</body>

""",
                unsafe_allow_html=True,
            )
        with Project:
            st.markdown(
                """<table border="1" style="border-collapse: collapse; width: 100%;">
   <thead>
      <tr>
         <th colspan="3" style="text-align: center; background-color: #E0FFFF; padding: 10px; color: rgb(0,0,0)">Project Initiation</th>
      </tr>
   </thead>
</table>
<table>
   <tbody>
      <tr>
         <td colspan="3" align="center" style="padding: 10px; background-color: #A9A9A9;color: rgb(0,0,0)">Part I: WhatsApp Chat Analysis</td>
      </tr>
      <tr>
         <td colspan = 1.5 style="vertical-align: top;">
            <b>1. Data Collection</b>
         </td>
         <td colspan = 2 style="vertical-align: top;">
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
         <td colspan = 2 style="vertical-align: top;">
            <ul>
               <li>Message Statistics and NLP</li>
               <li>Emoji Analysis and NLP</li>
               <li>Interactive Visualization and NLP</li>
               <li>Interdisciplinary Insights</li>
            </ul>
         </td>
      </tr>
      <tr>
   </tbody>
   </thead>
</table>
<table>
   <thead>
   <tbody>
      <td colspan="4" align="center" style="background-color: #A9A9A9; padding: 10px; color: rgb(0,0,0)">Part II: Sentiment Classification</td>
      </tr>
      <tr>
         <td style="vertical-align: top;">
            <b>1. Data Collection</b>
         </td>
         <td style="vertical-align: top;">
            <b>2. Preprocessing</b>
         </td>
         <td style="padding: 10px; color: rgb(255,255,255)">
            <b>3. Classification and Analysis</b>
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
         <td style="vertical-align: top;">
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
    # File uploader

    if page == "Upload File":
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
                            data.append([date, time, author, " ".join(messageBuffer)])
                        messageBuffer.clear()
                        date, time, author, message = message_data(line)
                        messageBuffer.append(message)
                    else:
                        messageBuffer.append(line)
                df = pd.DataFrame(data, columns=["Date", "Time", "Author", "Message"])
                df = df.dropna()

                # authors = df["Author"].unique()
                # author_mapping = {
                #     author: f"Sender {i+1}" for i, author in enumerate(authors)
                # }
                # df["Author"].replace(author_mapping, inplace=True)

                st.session_state.df = df
                new_df = pd.DataFrame(
                    data, columns=["Date", "Time", "Author", "Message"]
                )
                st.session_state.new_df = new_df
                st.session_state.visited_pages = set()
    # View DataFrame

    elif page == "View Chat":
        if "View DataFrame" not in st.session_state.visited_pages:
            if "df" in st.session_state:
                st.markdown(
                    "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Viewing Chat content as DataFrame: </h4><br>",
                    unsafe_allow_html=True,
                )
                with st.echo():
                    st.dataframe(st.session_state.df, width=1000, height=600)
            else:
                st.warning("Please upload the chat file, before proceeding.")
    # Process Chat

    elif page == "Process Chat":
        if "Process Chat" not in st.session_state.visited_pages:
            if "df" in st.session_state:
                import time

                with st.spinner("Loading..."):
                    time.sleep(2)
                st.subheader("Processing Chat Data")
                st.info(
                    "Please wait - Do not switch pages, Until process completes/terminated."
                )

                df = st.session_state.df
                df.reset_index(drop=True, inplace=True)

                # Define the progress bar
                progress_bar = st.progress(0)

                # Define the background task
                for i in range(95):
                    # Update the progress bar every 0.1 seconds
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)

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

                def remove_stopwords(message):
                    import nltk

                    nltk.download("stopwords")

                    stop_words = nltk.corpus.stopwords.words("english")
                    words = message.split()
                    filtered_words = [
                        word for word in words if word.lower() not in stop_words
                    ]
                    return " ".join(filtered_words)

                df["Message"] = df["Message"].apply(remove_stopwords)

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
                st.info("Process complete. Do navigate to <View Chat> page on sidebar.")
                st.session_state.visited_pages.add("Process Chat")

                # @st.cache_data

                def convert_df(df):
                    # IMPORTANT: Cache the conversion to prevent computation on every rerun

                    return df.to_csv().encode("utf-8")

                csv = convert_df(df)

                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name="df.csv",
                    mime="text/csv",
                )
            else:
                st.warning("Please upload the chat file, before proceeding.")
        else:
            st.warning(
                "You have already processed the chat data. Do navigate to <View Chat> page on sidebar."
            )
            df = st.session_state.df

            # @st.cache_data

            def convert_df(df):
                # IMPORTANT: Cache the conversion to prevent computation on every rerun

                return df.to_csv().encode("utf-8")

            csv = convert_df(df)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name="df.csv",
                mime="text/csv",
            )
    # Chat Insights

    elif page == "Chat Insights":
        Stats, Insights = st.tabs(["Stats", "Insights"])
        with Insights:

            def chat_in():
                if "df" in st.session_state:
                    df = st.session_state.df
                    st.markdown(
                        "<h5 style='font-size:20; color:#E0FFFF;font-family:monospace'><u>Chat Insights:</u></h5><br>",
                        unsafe_allow_html=True,
                    )

                    def count_message_by_sender():
                        st.text("1. Message Count of each sender in the chat:")
                        st.dataframe(
                            st.session_state.df["Author"].value_counts().head()
                        )

                    def num_total_days():
                        st.text("2. Total number of days the each sender was engaged:")
                        days_count_per_sender = df.groupby(["Author"])[
                            "Only_date"
                        ].nunique()
                        st.write(days_count_per_sender)
                        st.text("3. Total number of days the message were sent:")
                        total_days = df["Only_date"].nunique()

                        # Display the result

                        st.write(total_days)

                    def percentage_message_by_sender():
                        st.text(
                            "4. Percentage of message each sender sent in the chat:"
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
                        st.text("5. Total number of words present in the chat: ")
                        words = []
                        for message in df["Message"]:
                            words.extend(message.split())
                        st.write(len(words))

                    def media_count(df):
                        st.text("6. Total number of media files present in the chat: ")
                        df["Word_Count"] = df["Message"].str.count("media omitted")
                        WordCount = (df["Word_Count"] == 1).sum()
                        st.write(WordCount)

                    def url_count():
                        st.text(
                            "7. Total number of link(s)/url(s) present in the chat: "
                        )

                        new_df = st.session_state.new_df
                        url_regex_pattern = r"(https)?(://)?(?:www\.)\w+\.\w+(?:/\S*)?"

                        # Function to count URLs in a message

                        def count_urls(message):
                            return bool(re.findall(url_regex_pattern, message))

                        # Filter rows with URLs

                        df_with_urls = new_df[new_df["Message"].apply(count_urls)]

                        # Count total number of URLs in the DataFrame

                        total_url_count = (
                            df_with_urls["Message"].apply(count_urls).sum()
                        )

                        # Display the total number of URLs found in the DataFrame

                        st.write(total_url_count)

                        # Display the DataFrame with rows containing URLs

                        st.text("DataFrame with rows containing URLs:")
                        st.dataframe(df_with_urls)

                        # @st.cache_data

                        def convert_df(df):
                            # IMPORTANT: Cache the conversion to prevent computation on every rerun

                            return df.to_csv().encode("utf-8")

                        csv = convert_df(df_with_urls)

                        st.download_button(
                            label="Download as CSV",
                            data=csv,
                            file_name="url_count.csv",
                            mime="text/csv",
                        )

                    def count_emoji():

                        # from collections import Counter

                        st.text("8. Top emoji(s) used in the chat: ")

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
                        st.dataframe((dict(list(emoji_count.items()))))

                    def counting_emojis():
                        st.text("9. Emoji_count by sender: ")
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
                        st.text("10. Most frequent words:")

                        def rem_emojis(text):
                            return "".join(
                                char for char in text if char not in emoji.EMOJI_DATA
                            )

                        n_df = df["Message"].apply(rem_emojis)
                        with open("abusive_main.txt", "r") as file:
                            words_to_remove = file.read().splitlines()
                        for word in words_to_remove:
                            n_df = n_df[n_df != word]
                        n_df = n_df[n_df != "media omitted"]
                        n_df = n_df[n_df != ""]
                        word_freq = collections.Counter(n_df)
                        st.dataframe(word_freq.most_common())

                    # Executing Methods:

                    count_message_by_sender()
                    num_total_days()
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
        with Stats:

            if "df" in st.session_state:
                df = st.session_state.df

                st.markdown(
                    "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Viewing DataFrame Stats:</h4><br>",
                    unsafe_allow_html=True,
                )
                with st.echo():
                    st.write(st.session_state.df.describe())
                st.markdown(
                    """
                <h5 style="font-size:20; color:#E0FFFF;font-family:monospace"><u>Overview of the above description:</u></h5>
                <p style="font-size:18; color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
                The df.describe() function in pandas is like a summary report for your data. It gives you a quick overview of the main statistics for each column (or feature) in your DataFrame. Here's what it tells you:
	            <p style="font-size:18; font-weight:600;color:#E0FFFF;text-align:justify;text-justify: initial;font-family:monospace">
                By running df.describe(), we can quickly get a sense of the data's distribution, identify potential outliers, and understand the basic statistics of each feature in your DataFrame. It's a helpful starting point for data exploration and analysis in pandas.
                </p>""",
                    unsafe_allow_html=True,
                )
            else:
                st.warning("Please upload the chat file, before proceeding.")

    elif page == "Sentiment Analysis":
        if "df" in st.session_state:
            new_df = st.session_state.new_df
            import time

            with st.spinner("Loading..."):
                time.sleep(2)

            progress_bar = st.progress(0)
            for i in range(95):
                time.sleep(0.05)
                progress_bar.progress(i + 1)
            st.info(
                "Once you leave the page model will be reloaded (A drawback of streamlit framework)."
            )

            def rem_emojis(text):
                return "".join(char for char in text if char not in emoji.EMOJI_DATA)

            new_df = new_df[
                ~new_df["Message"].isin(
                    [
                        "This message was deleted",
                        "null",
                        "message deleted",
                        "deleted message",
                        "missed voice call",
                        "missed video call",
                        "",
                        "media omitted",
                    ]
                )
            ]
            new_df["Message"] = new_df["Message"].apply(rem_emojis)

            svm, lr, mnb = st.tabs(
                ["Support Vector Machine", "Logistic regression", "Multinomial NB"]
            )
            with svm:

                from joblib import load

                model_ = load("pipeline_svm.joblib")

                # Making Predictions
                st.text("Using model:" + str(model_))
                predictions = model_.predict(new_df["Message"])

                # converting predicted values to string labels
                sentiment_labels = {-1: "negative", 0: "neutral", 1: "positive"}
                predicted_sentiments = [sentiment_labels[pred] for pred in predictions]

                # creating final Dataframe
                result_df_svm = pd.DataFrame(
                    {
                        "Sender": new_df["Author"],
                        "Message": new_df["Message"],
                        "Sentiment": predicted_sentiments,
                    }
                )

                # displaying dataframe
                st.dataframe(result_df_svm, width=1500, height=700)
                st.markdown("<hr style= 'width : 5'>", unsafe_allow_html=True)

            with lr:
                from joblib import load

                model_ = load("pipeline_lr.joblib")

                # Making Predictions
                st.text("Using model:" + str(model_))
                predictions = model_.predict(new_df["Message"])

                # converting predicted values to string labels
                sentiment_labels = {-1: "negative", 0: "neutral", 1: "positive"}
                predicted_sentiments = [sentiment_labels[pred] for pred in predictions]

                # creating final Dataframe
                result_df_lr = pd.DataFrame(
                    {
                        "Sender": new_df["Author"],
                        "Message": new_df["Message"],
                        "Sentiment": predicted_sentiments,
                    }
                )

                # displaying dataframe
                st.dataframe(result_df_lr, width=1500, height=700)
                st.markdown("<hr style= 'width : 5'>", unsafe_allow_html=True)

            with mnb:
                from joblib import load

                model_ = load("multinomialNB799.joblib")

                # Making Predictions
                st.text("Using model:" + str(model_))
                predictions = model_.predict(new_df["Message"])

                # converting predicted values to string labels
                sentiment_labels = {-1: "negative", 0: "neutral", 1: "positive"}
                predicted_sentiments = [sentiment_labels[pred] for pred in predictions]

                # creating final Dataframe
                result_df = pd.DataFrame(
                    {
                        "Sender": new_df["Author"],
                        "Message": new_df["Message"],
                        "Sentiment": predicted_sentiments,
                    }
                )

                # displaying dataframe
                st.dataframe(result_df, width=1500, height=700)
                st.markdown("<hr style= 'width : 5'>", unsafe_allow_html=True)
            progress_bar.empty()

        else:
            st.warning("Please upload the chat file, before proceeding.")
    elif page == "Interactive Plots":

        if "df" in st.session_state:
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = st.session_state.df
            st.markdown(
                "<h4 style='font-size:18; color:#E0FFFF; text-align:justify;text-justify: initial;font-family:monospace'>Displaying Streamlit Interactive Plots: </h4><br>",
                unsafe_allow_html=True,
            )
            (
                Daily_Timeline,
                Monthly_Timeline,
                Busiest_Day,
                Busiest_Month,
                Busiest_Hours,
                Word_Cloud,
            ) = st.tabs(
                [
                    "Daily_Timeline",
                    "Monthly_Timeline",
                    "Busiest_Day",
                    "Busiest_Month",
                    "Busiest_Hours in a day",
                    "Word_Cloud",
                ]
            )

            with Busiest_Hours:

                def heatmap_():
                    plt.figure(figsize=(10, 5))
                    ax = sns.heatmap(
                        df.pivot_table(
                            index="Day_name",
                            columns="Hour_Period",
                            values="Message",
                            aggfunc="count",
                        ),
                        cmap="crest",
                        vmin=0,
                        vmax=25,
                        linewidths=0.5,
                        cbar=False,
                        square=True,
                    )
                    ax.set(xlabel="", ylabel="")
                    ax.xaxis.tick_top()
                    plt.xticks(rotation="vertical")
                    fig = plt.show()
                    # Display the heatmap using st.pyplot()

                    st.pyplot(fig)

                heatmap_()
            with Busiest_Month:

                def busyMonth():
                    busy_month = df["Month"].value_counts()
                    st.bar_chart(busy_month, height=600)

                busyMonth()
            with Busiest_Day:

                def busyDay():
                    busy_day = df["Day_name"].value_counts()
                    st.bar_chart(busy_day, height=600)

                busyDay()
            with Monthly_Timeline:

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
            with Daily_Timeline:

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
            with Word_Cloud:
                from wordcloud import WordCloud

                df = df[
                    ~df["Message"].isin(
                        [
                            "This message was deleted",
                            "null",
                            "message deleted",
                            "deleted message",
                            "missed voice call",
                            "missed video call",
                            "media omitted",
                            "",
                            " ",
                        ]
                    )
                ]

                def wordcloud_():
                    words = df["Message"]
                    text = " ".join(words)
                    # Create a WordCloud object with increased max_words

                    wordcloud = WordCloud(
                        width=1400, height=800, background_color="white", max_words=100
                    ).generate(text)

                    # Plot the WordCloud

                    plt.figure(figsize=(10, 10))
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    fig = plt.show()
                    st.pyplot(fig)

                wordcloud_()

                def wordcloud2():
                    n_df = df["Message"]
                    with open("abusive_main.txt", "r") as file:
                        words_to_remove = file.read().splitlines()
                    for word in words_to_remove:
                        n_df = n_df[n_df != word]
                    n_df = n_df[n_df != "media omitted"]
                    n_df = n_df[n_df != "null"]

                    wordcloud = WordCloud(
                        width=1400, height=800, background_color="white", max_words=50
                    ).generate(" ".join(n_df))

                    plt.figure(figsize=(10, 10))
                    plt.imshow(wordcloud, interpolation="bilinear")
                    plt.axis("off")
                    fig = plt.show()
                    st.pyplot(fig)

                wordcloud2()

        else:
            st.warning("Please upload the chat file, before proceeding.")


if __name__ == "__main__":
    main()
