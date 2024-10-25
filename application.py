from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)


def load_model():
    with open('basic_classifier.pkl', 'rb') as fid:
            model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
            vectorizer = pickle.load(vd)
    return model, vectorizer

model, vectorizer = load_model()

@application.route("/")
def index():
    return "Your Flask Application Runs!! V1.0"

@application.route("/predict", methods=['POST'])
def predict():
        data = request.get_json()
        input_text = data.get("text", "")
        prediction = model.predict(vectorizer.transform([input_text]))[0]

        return jsonify({"prediction": prediction})

if __name__ == "__main__":
    application.run(port=5000, debug=True)