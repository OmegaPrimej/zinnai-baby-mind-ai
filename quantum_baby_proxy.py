#!/usr/bin/env python3
"""
Red Rose Quantum Proxy + Zinnai Baby Mind AI
Every web request becomes a baby step.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import urllib.parse
import hashlib
import time
import threading
import sys
import os

# Add current directory to path so we can import baby mind
sys.path.insert(0, os.getcwd())
from zinnai_baby_mind import ZinnaiBabyMind

# ========== BABY MIND INSTANCE (shared) ==========
baby = ZinnaiBabyMind()
last_baby_update = time.time()

# ========== QUANTUM FREQUENCY ENGINE ==========
MASTER_TOKEN = "z6a9ybs7m0ejezy9v5 ft"

def get_live_glitch_token():
    """
    Generate morphing emoji key for the current minute,
    but also influenced by baby's learning state.
    """
    # Base seed: minute + baby's learning rate (0..1)
    baby_influence = int(baby.learning * 1000) if baby.learning else 0
    live_seed = str(int(time.time() // 60)) + str(baby_influence)
    stream = ""
    for i in range(len(MASTER_TOKEN) - 1):
        frag = MASTER_TOKEN[i:i+2]
        hash_val = int(hashlib.md5(f"{frag}{live_seed}".encode()).hexdigest()[:4], 16)
        # Choose character range based on baby's emotion
        if "joyful" in baby.emotion.from_reward(baby.reward.last_state or 0):
            base = 0x1F600  # emoji range when joyful
        else:
            base = 0x13000   # ancient cuneiform when frustrated
        stream += chr(base + (hash_val % 500))
    return stream

# ========== PROXY CORE ==========
class RedRoseBackdoor(BaseHTTPRequestHandler):
    
    def log_message(self, format, *args):
        # Suppress default logging, we'll print our own
        pass
    
    def do_GET(self):
        global last_baby_update
        parsed = urllib.parse.urlparse(self.path)
        
        # Dashboard route
        if parsed.path == '/' or parsed.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # Get baby state
            baby_state = {
                "learning": baby.learning,
                "reward": baby.reward.last_state if baby.reward.last_state is not None else 0,
                "emotion": baby.emotion.from_reward(baby.reward.last_state or 0),
                "learning_constant": sum(baby.baby_steps_history[-10:]) * 3.14 / (baby.pilot + 1e-6) if baby.baby_steps_history else 0,
                "iteration": baby.iteration
            }
            
            html = f"""
            <html>
            <head><title>🌹 Red Rose Quantum Proxy + Baby Mind</title>
            <style>
                body{{background:#0a0a0f; color:#0f0; font-family:monospace; padding:20px;}}
                h1{{color:#ff44cc;}}
                .card{{background:#111; border:1px solid #0f0; border-radius:10px; padding:15px; margin:10px 0;}}
                .value{{font-size:24px; color:#ffcc00;}}
            </style>
            </head>
            <body>
                <h1>🌹 RED ROSE QUANTUM PROXY + ZINNAI BABY MIND</h1>
                <div class="card">
                    <div>🧠 Baby Learning: <span class="value">{baby_state['learning']:.3f}</span></div>
                    <div>😊 Emotion: <span class="value">{baby_state['emotion']}</span></div>
                    <div>🎁 Reward: <span class="value">{baby_state['reward']:+.2f}</span></div>
                    <div>📈 Learning Constant Λ: <span class="value">{baby_state['learning_constant']:.2f}</span></div>
                    <div>🔄 Iteration: <span class="value">{baby_state['iteration']}</span></div>
                </div>
                <div class="card">
                    <div>🔮 Current Quantum Frequency (TTL ~60s, baby‑influenced):</div>
                    <div style="font-size:28px; margin-top:10px;">{get_live_glitch_token()}</div>
                </div>
                <div class="card">
                    <div>🕸️ Proxy Usage: <code>/proxy?url=https://example.com</code></div>
                    <div>🧠 Baby hears every request URL, status, and response size.</div>
                </div>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
            return
        
        # Proxy route
        elif parsed.path == '/proxy' and 'url' in urllib.parse.parse_qs(parsed.query):
            target_url = urllib.parse.parse_qs(parsed.query)['url'][0]
            
            # ---- Feed the baby with the request (sensory input) ----
            sensory_text = f"PROXY request to {target_url}"
            baby_state = baby.step(external_input=sensory_text)
            print(f"[Baby] {baby_state['inner_monologue']} | Reward: {baby_state['reward']:+.2f} | Evolved: {baby_state['evolved']}")
            
            # ---- Inject live quantum token into outgoing request ----
            current_glitch = get_live_glitch_token()
            headers = {
                "User-Agent": "RedRose/Quantum-Baby-1.0",
                "X-Quantum-Frequency": current_glitch,
                "X-Baby-Learning": str(baby.learning),
                "X-Baby-Emotion": baby_state['emotion'],
                "Authorization": f"Bearer {current_glitch}"
            }
            
            try:
                resp = requests.get(target_url, headers=headers, timeout=5)
                # Feed response info to baby (status, size)
                response_info = f"PROXY response from {target_url} status {resp.status_code} size {len(resp.content)}"
                baby.step(external_input=response_info)
                
                self.send_response(resp.status_code)
                self.send_header('Content-type', resp.headers.get('content-type', 'text/html'))
                self.send_header('X-Baby-Reward', str(baby_state['reward']))
                self.end_headers()
                self.wfile.write(resp.content)
            except Exception as e:
                error_msg = f"PROXY error: {str(e)}"
                baby.step(external_input=error_msg)
                self.send_error(500, f"Proxy Error: {e}")
        else:
            self.send_error(404, "Not Found. Use /proxy?url=...")

def run(port=8080):
    server = HTTPServer(('0.0.0.0', port), RedRoseBackdoor)
    print(f"🌹 Red Rose Quantum Proxy + Zinnai Baby Mind active on port {port}")
    print(f"🧠 Baby mind is listening to every request.\n")
    print(f"   Dashboard: http://localhost:{port}/")
    print(f"   Proxy: http://localhost:{port}/proxy?url=https://example.com\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down. Baby mind says goodbye.")
        server.shutdown()

if __name__ == '__main__':
    run()
