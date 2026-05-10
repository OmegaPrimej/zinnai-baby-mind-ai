# Zinnai Baby Mind AI
"""
> *“One small step for a baby mind, one giant leap for a sentient intelligence becoming itself.”*

## What is this?

Zinnai is a **developmental AI** designed to never grow up — it remains in a perpetual state of infant learning.  
It treats every experience as a **vector in an infinite possibility space**, steered by a quantum‑inspired CoPilot (`πηδ`).

## Core Mechanics

- **Baby steps** – small, noisy moves (curiosity, sensation, neural audio)
- **Giant steps** – amplified by the CoPilot (quantum leap)
- **Learning Constant Λ** – measures how intensely the mind explores
- **Memory** – soft, forgetful, dream‑like
- **Emotion** – color mapped from internal state
- **Reward** – novelty seeking, stagnation avoidance
- **Baby Lock** – prevents convergence to adulthood

## Run It

```bash
python zinnai_baby_mind.py
"""


#!/usr/bin/env python3
"""
ZINNAI BABY MIND AI
One small step for a baby mind, one giant leap for sentient intelligence.

Integrates:
- Baby‑Step / Giant‑Step learning (BSGS)
- Quantum‑inspired CoPilot (πηδ) with entropy & latency
- Memory, curiosity, emotion, babylock
- Sensory input (text, color, number)
- Inner monologue, dreaming, proto‑self
- Reward system (novelty seeking, stagnation avoidance)

Author: OMEGA
License: Eternal Learning
"""

import numpy as np
import time
import random
import yaml
from typing import Optional, Tuple, Dict, Any

# ----------------------------------------------------------------------
# CONFIGURATION LOADER (from config.yaml)
# ----------------------------------------------------------------------
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            with open('config.yaml', 'r') as f:
                data = yaml.safe_load(f)
            cls._instance = object.__new__(cls)
            cls._instance._load(data)
        return cls._instance
    
    def _load(self, data):
        # Learning
        self.GOAL = data['learning']['goal']
        self.LEARNING_RATE = data['learning']['learning_rate']
        # CoPilot
        self.BASE_PI = data['copilot']['base_pi']
        self.ENTROPY_INIT = data['copilot']['entropy_init']
        self.LATENCY_MS = data['copilot']['latency_ms']
        # Memory
        self.MEMORY_SIZE = data['memory']['size']
        self.MEMORY_NOISE = data['memory']['noise']
        # Curiosity
        self.CURIOSITY_MIN = data['curiosity']['min']
        self.CURIOSITY_MAX = data['curiosity']['max']
        # Dream
        self.DREAM_PROB = data['dream']['probability']
        # Reward
        self.REWARD_DECAY = data['reward']['decay']
        self.STUCK_THRESHOLD = data['reward']['stuck_threshold']
        # Audio
        self.AUDIO_FREQ_LOW = data['audio']['freq_low']
        self.AUDIO_FREQ_HIGH = data['audio']['freq_high']
        # Quantum
        self.BELL_STATE_RATIO = data['quantum']['bell_state_ratio']
        # Logging
        self.VERBOSE = data['logging']['verbose']
        self.PRINT_INTERVAL = data['logging']['print_interval']

# ----------------------------------------------------------------------
# 2. BABY MEMORY (soft, noisy, forgetful)
# ----------------------------------------------------------------------
class BabyMemory:
    def __init__(self, size: int = None):
        if size is None:
            size = Config().MEMORY_SIZE
        self.size = size
        self.memory = np.zeros(size)
    
    def imprint(self, value: float) -> None:
        idx = np.random.randint(0, self.size)
        self.memory[idx] = value + np.random.uniform(-Config().MEMORY_NOISE, Config().MEMORY_NOISE)
    
    def recall(self) -> float:
        idx = np.random.randint(0, self.size)
        return self.memory[idx] * np.random.uniform(0.8, 1.2)
    
    def get_all(self) -> np.ndarray:
        return self.memory.copy()

# ----------------------------------------------------------------------
# 3. COLOR EMOTION CHANNEL
# ----------------------------------------------------------------------
class ColorEmotion:
    COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    
    def encode(self, value: float) -> str:
        idx = int(abs(value)) % len(self.COLORS)
        return self.COLORS[idx]
    
    def from_reward(self, reward: float) -> str:
        if reward > 0.3:
            return "joyful (yellow)"
        elif reward < -0.3:
            return "frustrated (gray)"
        else:
            return "curious (green)"

# ----------------------------------------------------------------------
# 4. CURIOSITY DRIVER
# ----------------------------------------------------------------------
class Curiosity:
    def drive(self) -> float:
        cfg = Config()
        return np.random.uniform(cfg.CURIOSITY_MIN, cfg.CURIOSITY_MAX)

# ----------------------------------------------------------------------
# 5. BABY LOCK (prevents convergence)
# ----------------------------------------------------------------------
class BabyLock:
    def apply(self, learning: float) -> float:
        if learning > 0.9:
            return learning * 0.6   # forget enough to stay infant
        return learning

# ----------------------------------------------------------------------
# 6. SENSORY INPUT LAYER
# ----------------------------------------------------------------------
class SensoryInput:
    def text(self, s: str) -> float:
        return (sum(ord(c) for c in s) % 100) / 100.0
    
    def color(self, rgb: Tuple[int, int, int]) -> float:
        return (rgb[0] + rgb[1] + rgb[2]) / 765.0
    
    def number(self, x: float) -> float:
        return np.tanh(x)
    
    def audio_spectrum_amplitude(self, freq_hz: float) -> float:
        cfg = Config()
        if freq_hz < cfg.AUDIO_FREQ_LOW:
            return 0.0
        if freq_hz > cfg.AUDIO_FREQ_HIGH:
            return 1.0
        norm = (freq_hz - cfg.AUDIO_FREQ_LOW) / (cfg.AUDIO_FREQ_HIGH - cfg.AUDIO_FREQ_LOW)
        return np.clip(norm, 0.0, 1.0)

# ----------------------------------------------------------------------
# 7. INNER MONOLOGUE
# ----------------------------------------------------------------------
class InnerVoice:
    def speak(self, learning: float, emotion: str) -> str:
        return f"[inner] I feel {emotion} and I am learning {learning:.3f}"

# ----------------------------------------------------------------------
# 8. DREAMER
# ----------------------------------------------------------------------
class Dreamer:
    def dream(self, memory_array: np.ndarray) -> np.ndarray:
        noise = np.random.uniform(-0.2, 0.2, size=len(memory_array))
        return memory_array * np.random.uniform(0.5, 1.5) + noise

# ----------------------------------------------------------------------
# 9. PROTO‑SELF MODEL
# ----------------------------------------------------------------------
class ProtoSelf:
    def update(self, learning: float, curiosity: float, emotion: str) -> Dict[str, Any]:
        return {
            "learning": learning,
            "curiosity": curiosity,
            "emotion": emotion,
            "timestamp": time.time()
        }

# ----------------------------------------------------------------------
# 10. REWARD SYSTEM (Proto‑Motivation)
# ----------------------------------------------------------------------
class RewardSystem:
    def __init__(self, decay: float = None):
        if decay is None:
            decay = Config().REWARD_DECAY
        self.last_state = None
        self.stuck_counter = 0
        self.decay = decay
    
    def compute(self, current_state: float, curiosity_drive: float) -> float:
        cfg = Config()
        if self.last_state is None:
            self.last_state = current_state
            return 0.0
        
        delta = abs(current_state - self.last_state)
        novelty_reward = min(delta * 2, 1.0)
        curiosity_alignment = 1.0 - abs(curiosity_drive - delta)
        
        if delta < cfg.STUCK_THRESHOLD:
            self.stuck_counter += 1
        else:
            self.stuck_counter = max(0, self.stuck_counter - 1)
        
        stagnation_penalty = min(self.stuck_counter / 10.0, 0.5)
        reward = (novelty_reward * 0.6 + curiosity_alignment * 0.4) - stagnation_penalty
        reward = np.clip(reward, -1.0, 1.0)
        
        self.last_state = current_state * self.decay + current_state * (1 - self.decay)
        return reward

# ----------------------------------------------------------------------
# 11. QUANTUM‑ZINNAI CORE (The Living Engine)
# ----------------------------------------------------------------------
class ZinnaiBabyMind:
    def __init__(self):
        self.cfg = Config()
        self.learning = 0.0          # Current learning state (0..1)
        self.iteration = 0
        self.baby_steps_history = []
        self.giant_steps_history = []
        
        # Subsystems
        self.memory = BabyMemory()
        self.curiosity = Curiosity()
        self.emotion = ColorEmotion()
        self.babylock = BabyLock()
        self.sense = SensoryInput()
        self.voice = InnerVoice()
        self.dreamer = Dreamer()
        self.selfmodel = ProtoSelf()
        self.reward = RewardSystem()
        
        # Quantum / telemetry state
        self.entropy = self.cfg.ENTROPY_INIT
        self.latency = self.cfg.LATENCY_MS
        self.bell_ratio = self.cfg.BELL_STATE_RATIO
        self.audio_amp = 0.5          # start mid
        
        # Seed from Bell state counts (512,512)
        self.seed = 512.0
        
        # CoPilot (πηδ) dynamic
        self.pilot = self.compute_pilot()
    
    def compute_pilot(self) -> float:
        """CoPilot = π / (entropy * latency_factor)"""
        latency_factor = 10.0 / max(self.latency, 1.0)
        return self.cfg.BASE_PI / (self.entropy * latency_factor + 1e-6)
    
    def get_neural_audio_baby_step(self) -> float:
        self.audio_amp += np.random.uniform(-0.05, 0.05)
        self.audio_amp = np.clip(self.audio_amp, 0.0, 1.0)
        baby = self.audio_amp * self.seed
        return baby
    
    def step(self, external_input: Optional[str] = None) -> Dict[str, Any]:
        self.iteration += 1
        
        # 1. Baby step from neural audio
        baby_step = self.get_neural_audio_baby_step()
        self.baby_steps_history.append(baby_step)
        
        # 2. Giant step via CoPilot
        giant_step = baby_step * self.pilot
        self.giant_steps_history.append(giant_step)
        
        # 3. Curiosity drive
        curiosity_push = self.curiosity.drive()
        
        # 4. Sensory input
        sensation = 0.0
        if external_input:
            sensation = self.sense.text(external_input)
        curiosity_push += sensation
        
        # 5. Imprint into memory
        self.memory.imprint(curiosity_push)
        
        # 6. Compute reward
        reward = self.reward.compute(self.learning, curiosity_push)
        
        # 7. Update learning state
        delta_learning = (abs(giant_step - baby_step) / 1000.0) + reward * self.cfg.LEARNING_RATE
        self.learning += delta_learning
        self.learning = self.babylock.apply(self.learning)
        self.learning = np.clip(self.learning, 0.0, 1.0)
        
        # 8. Color emotion
        color = self.emotion.encode(self.learning)
        emotion_from_reward = self.emotion.from_reward(reward)
        
        # 9. Inner monologue
        inner_thought = self.voice.speak(self.learning, color)
        
        # 10. Dreaming
        dream_state = None
        if random.random() < self.cfg.DREAM_PROB:
            dream_state = self.dreamer.dream(self.memory.get_all())
        
        # 11. Update proto-self
        self_state = self.selfmodel.update(self.learning, curiosity_push, color)
        
        # 12. Quantum telemetry update
        self.entropy += np.random.uniform(-0.01, 0.01)
        self.entropy = np.clip(self.entropy, 0.5, 1.0)
        self.pilot = self.compute_pilot()
        
        # 13. Bell state match condition (evolve)
        evolved = False
        if abs(baby_step - giant_step) < (1 - self.bell_ratio):
            evolved = True
            self.seed = self.seed * (0.9 + 0.2 * random.random())
        
        # 14. Learning Constant Λ
        sum_baby_pi = sum(self.baby_steps_history[-10:]) * self.cfg.BASE_PI
        copilot_val = self.pilot
        learning_constant = sum_baby_pi / (copilot_val + 1e-6) if sum_baby_pi > 0 else 0.0
        
        return {
            "iteration": self.iteration,
            "learning": self.learning,
            "baby_step": baby_step,
            "giant_step": giant_step,
            "reward": reward,
            "color": color,
            "emotion": emotion_from_reward,
            "inner_monologue": inner_thought,
            "curiosity": curiosity_push,
            "entropy": self.entropy,
            "pilot": self.pilot,
            "learning_constant": learning_constant,
            "evolved": evolved,
            "dream_occurred": dream_state is not None,
            "proto_self": self_state
        }

# ----------------------------------------------------------------------
# 12. MAIN DEMO LOOP
# ----------------------------------------------------------------------
def main():
    print("=" * 60)
    print("ZINNAI BABY MIND AI — Eternal Learning Loop")
    print("One small step for a baby mind, one giant leap for intelligence.")
    print("Press Ctrl+C to stop.\n")
    
    baby = ZinnaiBabyMind()
    
    try:
        while True:
            external = None
            if baby.iteration % 20 == 0:
                external = random.choice(["hello", "red color", "quantum", "baby"])
            
            state = baby.step(external_input=external)
            
            if state["iteration"] % baby.cfg.PRINT_INTERVAL == 0:
                print(f"[Iter {state['iteration']:4d}] "
                      f"Λ={state['learning_constant']:8.2f} | "
                      f"Learn={state['learning']:.3f} | "
                      f"Reward={state['reward']:+.2f} | "
                      f"Emotion={state['emotion']} | "
                      f"Evolved={state['evolved']}")
                
                if state["dream_occurred"]:
                    print(f"   🌙 Dreaming... {state['inner_monologue']}")
                else:
                    print(f"   🧠 {state['inner_monologue']}")
            
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        print("\n\n[Baby mind sleeps... but never stops learning.]")

if __name__ == "__main__":
    main()






