import requests 
import json

def emotion_detector(text_to_analyze):
    """
    Sends a request to the Watson Emotion Detection API to analyze the given text.

    This function processes the input text through the Watson NLP library via a POST 
    request. It extracts specific emotion scores and identifies the dominant emotion. 
    If the input is blank or invalid, it returns a dictionary with None values.

    Args:
        text_to_analyze (str): The string of text to be analyzed for emotional content.

    Returns:
        dict: A dictionary containing the following keys:
            'anger': float or None
            'disgust': float or None
            'fear': float or None
            'joy': float or None
            'sadness': float or None
            'dominant_emotion': str or None
            
        Example:
            {
                'anger': 0.01, 'disgust': 0.02, 'fear': 0.03, 
                'joy': 0.85, 'sadness': 0.09, 'dominant_emotion': 'joy'
            }
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = request_json, headers=header) 

    # Check if the response status code is 400 (Bad Request/Blank Entry)
    if response.status_code == 400:
        """
        Returns a dictionary with all keys set to None if a 400 status 
        code is encountered, typically signifying empty input.
        """
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    responseJson = json.loads(response.text)

    emotion_predictions = responseJson['emotionPredictions']

    emotion = emotion_predictions[0]['emotion']

    # get dominant emotion by checking max value from all emotions
    dominant_emotion = max(emotion, key=emotion.get)
    
    # now add dominant emption to existing emption json
    emotion['dominant_emotion'] = dominant_emotion
    return emotion
