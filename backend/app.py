# backend/app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and feature list
model = joblib.load('backend/pmes_voter_turnout_model.pkl')
model_features = joblib.load('backend/model_features.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=model_features, fill_value=0)
    proba = model.predict_proba(df)[0][1]
    risk = "High" if proba < 0.4 else "Medium" if proba < 0.7 else "Low"
    return jsonify({
        'voting_likelihood': round(proba, 3),
        'apathy_risk': risk,
        'recommendation': get_recommendation(risk)
    })

def get_recommendation(risk):
    return {
        'High': 'Send motivational quiz + peer challenge',
        'Medium': 'Share candidate match quiz',
        'Low': 'Send “I Voted” badge reminder'
    }[risk]

@app.route('/gamify/complete_task', methods=['POST'])
def complete_task():
    user_id = request.json['user_id']
    task = request.json['task']
    rewards = {
        'quiz': {'points': 50, 'badge': 'Knowledge Seeker'},
        'refer': {'points': 100, 'reward': '100MB airtime'},
        'register': {'points': 200, 'badge': 'Civic Champion'}
    }
    return jsonify({
        'status': 'success',
        'task': task,
        'reward': rewards.get(task, {}),
        'total_points': 350
    })

# backend/app.py (last lines)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))