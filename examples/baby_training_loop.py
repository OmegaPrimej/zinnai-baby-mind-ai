#!/usr/bin/env python3
"""
Headless batch training for Zinnai Baby Mind AI.
Runs for N iterations, logs learning constant, reward, and evolution events.
"""

import sys
import os
import time
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zinnai_baby_mind import ZinnaiBabyMind

def main():
    print("🧠 ZINNAI BABY MIND — Batch Training Mode")
    print("=" * 50)
    
    # Configuration
    iterations = int(os.environ.get("ZINNAI_ITERATIONS", 1000))
    log_file = f"training_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    baby = ZinnaiBabyMind()
    log_data = []
    
    print(f"Running {iterations} iterations...")
    start_time = time.time()
    
    for i in range(iterations):
        # Optional: inject random text every 20 steps
        if i % 20 == 0:
            external = ["hello", "red", "quantum", "baby", "color"][i % 5]
        else:
            external = None
        
        state = baby.step(external_input=external)
        
        # Log every 10 steps
        if i % 10 == 0:
            log_data.append({
                "iteration": i,
                "learning": state["learning"],
                "learning_constant": state["learning_constant"],
                "reward": state["reward"],
                "emotion": state["emotion"],
                "evolved": state["evolved"],
                "entropy": state["entropy"],
                "pilot": state["pilot"]
            })
            print(f"[{i:4d}] Λ={state['learning_constant']:.2f} | Learn={state['learning']:.3f} | Evolved={state['evolved']}")
    
    elapsed = time.time() - start_time
    
    # Save log
    with open(log_file, "w") as f:
        json.dump(log_data, f, indent=2)
    
    print(f"\n✅ Training complete. {iterations} iterations in {elapsed:.2f} seconds.")
    print(f"📊 Log saved to {log_file}")

if __name__ == "__main__":
    main()
