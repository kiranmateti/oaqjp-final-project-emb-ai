import requests 
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_json = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = request_json, headers=header) 
    responseJson = json.loads(response.text)

    emotion_predictions = responseJson['emotionPredictions']

    emotion = emotion_predictions[0]['emotion']

    # get dominant emotion by checking max value from all emotions
    dominant_emotion = max(emotion, key=emotion.get)
    
    # now add dominant emption to existing emption json
    emotion['dominant_emotion'] = dominant_emotion
    return emotion
