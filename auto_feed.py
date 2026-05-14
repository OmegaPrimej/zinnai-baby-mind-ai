#!/usr/bin/env python3
import sys, os, time, random
sys.path.insert(0, os.getcwd())
from zinnai_baby_mind import ZinnaiBabyMind

def main():
    baby = ZinnaiBabyMind()
    words = ['fire','aurora','quantum','💀','hello','color','noise','dream','evolve','singularity','iota','Ω','frustrated','curious','baby','mind','eternal','learning','spider','multiverse','dagger','wire']
    print("🤖 Auto-feeder running. Press Ctrl+C to stop.\n")
    try:
        while True:
            w = random.choice(words)
            s = baby.step(w)
            print(f"You: {w}\n👶 Baby: {s['inner_monologue']}\n   [Λ={s['learning_constant']:.2f} | Reward={s['reward']:+.2f} | Evolved={s['evolved']}]\n")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()
