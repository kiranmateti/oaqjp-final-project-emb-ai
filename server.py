from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    text_to_analyze = request.args.get('textToAnalyze')

    emotion = emotion_detector(text_to_analyze)

    dominant_emotion = emotion['dominant_emotion'] 
    # delete the dominant emotion from JSON
    del emotion['dominant_emotion']

    #convert JSON to string and remove start and last aquare brackets
    formatted_resp = str(emotion)[1:-1]
    
    return "For the given statement, the system response is {}. The dominant emotion is <b>{}</b>.".format(formatted_resp, dominant_emotion)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
