#!/usr/bin/env python3
"""
Interactive console demo for Zinnai Baby Mind AI.
Type messages to the baby and watch it respond with inner monologue and emotion.
"""

import sys
import os

# Add parent directory to path so we can import the main module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zinnai_baby_mind import ZinnaiBabyMind

def main():
    print("\n" + "=" * 60)
    print("🧠 ZINNAI BABY MIND — Interactive Chat")
    print("Type your message and the baby will respond.")
    print("Commands: 'quit' to exit, 'state' to see full state.")
    print("=" * 60 + "\n")

    baby = ZinnaiBabyMind()

    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("\n👶 Baby mind goes to sleep... (but never stops learning)")
            break
        elif user_input.lower() == 'state':
            # Show current snapshot (no step taken)
            print(f"Learning: {baby.learning:.3f}, Iteration: {baby.iteration}, Entropy: {baby.entropy:.3f}")
            continue
        elif not user_input:
            continue
        
        # Perform one learning step with external input
        state = baby.step(external_input=user_input)
        
        print(f"👶 Baby: {state['inner_monologue']}")
        print(f"   [Emotion: {state['emotion']} | Reward: {state['reward']:+.2f} | Λ: {state['learning_constant']:.2f}]")
        if state['evolved']:
            print("   ⚡ EVOLUTION! Baby step matched giant step — singularity point ι reached!")
        print()

if __name__ == "__main__":
    main()
