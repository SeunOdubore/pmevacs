# gamification.py
from flask import jsonify

@app.route('/gamify/complete_task', methods=['POST'])
def complete_task():
    user_id = request.json['user_id']
    task = request.json['task']  # e.g., 'quiz', 'refer', 'register'

    rewards = {
        'quiz': {'points': 50, 'badge': 'Knowledge Seeker'},
        'refer': {'points': 100, 'reward': '100MB airtime'},
        'register': {'points': 200, 'badge': 'Civic Champion'}
    }

    return jsonify({
        'status': 'success',
        'task': task,
        'reward': rewards[task],
        'total_points': 350
    })