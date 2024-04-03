from flask import *
import pickle
import nltk
import re

nltk.download('stopwords')

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

app = Flask(__name__)

def preprocess(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text) # Remove @mentions
    text = re.sub(r'#', '', text) # Remove hashtags
    text = re.sub(r'RT[\s]+', '', text) # Remove retweets
    text = re.sub(r'https?:\/\/\S+', '', text) # Remove hyperlinks
    text = re.sub(r'\n', '', text) # Remove newlines
    text = re.sub(r'[^\w\s]', '', text) # Remove punctuation
    text = re.sub(r'\d+', '', text) # Remove digits
    text = ' '.join([word for word in text.split() if word not in stop_words]) # remove stop words
    return text


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", sentiment = "", data="")


@app.route('/process_data', methods=['POST'])
def process_data():
    data = org = request.form['input_name']
    data = preprocess(data)
    with open('models/roberta.pkl', 'rb') as file:
        model = pickle.load(file)
    sentiment = model.predict(data)
    print(sentiment)
    map = {'LABEL_0': "Negative", 'LABEL_1': "Neutral", 'LABEL_2': "Positive"}
    senti = map[sentiment[0]['label']]
    print(senti)
    return render_template("index.html", sentiment = senti, data=org)


if __name__ == '__main__':
    app.run(debug=True)
