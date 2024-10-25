import requests
import time
import csv

url = "http://Serve-sentiment-env-1.eba-zm6xumcq.us-east-2.elasticbeanstalk.com/predict"  # Replace with actual URL


def get_prediction(text):

    response = requests.post(url, json={"text": text})
    if response.status_code == 200:
        result = response.json()['prediction']
        return result
    else:
        return None


if __name__ == "__main__":
    text = "is this real or fake?"
    print(get_prediction(text))