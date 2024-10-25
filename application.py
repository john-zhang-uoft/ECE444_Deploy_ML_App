from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Your Flask ML App Works!"

@app.route('predict', methods=['POST'])
def predict():
    data = request.get_json()
    transformed_text = vectorizer.transform(data['text'])
    prediction = model.predict(transformed_text)
    return jsonify({'prediction': prediction.tolist()})

def load_model():
    loaded_model = None
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)

    vectorizer = None
    with open('vectorizer.pkl', 'rb') as fid:
        vectorizer = pickle.load(fid)
    return loaded_model, vectorizer

if __name__ == "__main__":
    model, vectorizer = load_model()
    app.run(port=5000, debug=True)
