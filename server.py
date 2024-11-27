"""
This module contains the Flask web application for emotion detection. 
It exposes an API at '/emotionDetector' that processes a given statement 
and returns the dominant emotion along with detailed emotion scores.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route('/emotionDetector')
def emotion_detector_api():
    """
    This function processes the input statement, runs it through the emotion detector,
    and returns the dominant emotion with a formatted message.
    """
    text_to_detect = request.args.get('textToAnalyze')
    formated_response  = emotion_detector(text_to_detect)

    if formated_response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )
@app.route('/')
def index():
    """
    This function serves the index page to the user.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
