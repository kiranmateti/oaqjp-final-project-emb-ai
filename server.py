"""
This module implements a Flask server for an Emotion Detection application.
It provides routes to render the index page and to process text for
emotion analysis using an external detection service.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Analyzes the user-provided text for emotions and returns a formatted response.

    Receives text from a GET request, calls the emotion_detector function,
    and returns a string displaying individual scores and the dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function
    emotion = emotion_detector(text_to_analyze)

    # Extract the dominant emotion
    dominant_emotion = emotion['dominant_emotion']

    # Check for invalid or blank input
    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    # Remove the dominant_emotion key to format the remaining scores
    del emotion['dominant_emotion']

    # Convert the dictionary to a string and strip curly braces
    formatted_resp = str(emotion)[1:-1]

    # Return the final success message with the dominant emotion in bold
    return (
        f"For the given statement, the system response is {formatted_resp}. "
        f"The dominant emotion is <b>{dominant_emotion}</b>."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    