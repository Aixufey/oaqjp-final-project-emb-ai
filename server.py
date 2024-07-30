from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def render_index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    return f"""For the given statement, the system response is:
     <ul>
        <li>'anger': {response['anger']}</li>
        <li>'disgust': {response['disgust']}</li> 
        <li>'fear': {response['fear']}</li>
        <li>'joy': {response['joy']}</li>
        <li>'sadness': {response['sadness']}</li>
     </ul>
     The dominant emotion is <strong>{response['dominant_emotion']}</strong>
     """
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)