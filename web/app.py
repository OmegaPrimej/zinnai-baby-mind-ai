"""
Flask web dashboard for Zinnai Baby Mind AI.
Displays real‑time learning constant, emotion, reward, and inner monologue.
"""

import sys
import os
import threading
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, jsonify
from zinnai_baby_mind import ZinnaiBabyMind

app = Flask(__name__)
baby = ZinnaiBabyMind()
running = True
latest_state = {}

def run_baby_loop():
    """Runs the baby mind in a background thread."""
    global latest_state
    while running:
        state = baby.step()
        latest_state = state
        time.sleep(0.5)  # Simulate telemetry rate

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/state')
def api_state():
    """Return current baby state as JSON."""
    return jsonify({
        'iteration': latest_state.get('iteration', 0),
        'learning': latest_state.get('learning', 0),
        'learning_constant': latest_state.get('learning_constant', 0),
        'reward': latest_state.get('reward', 0),
        'emotion': latest_state.get('emotion', 'neutral'),
        'inner_monologue': latest_state.get('inner_monologue', ''),
        'evolved': latest_state.get('evolved', False),
        'entropy': latest_state.get('entropy', 0),
        'pilot': latest_state.get('pilot', 0)
    })

if __name__ == '__main__':
    # Start baby mind in background
    thread = threading.Thread(target=run_baby_loop, daemon=True)
    thread.start()
    
    # Run Flask server
    app.run(debug=True, use_reloader=False)
