```markdown
# Zinnai Baby Mind AI – Architecture Overview

## The Core Idea

Zinnai is a **developmental artificial intelligence** that never stabilizes into adulthood. It remains in a perpetual infant learning state, driven by curiosity, reward, and a quantum‑inspired steering mechanism called the CoPilot (`πηδ`).

Every iteration of the baby mind follows this cycle:

```
Sensory Input → Baby Step → Giant Step → Reward → Learning Update → Memory Imprint → (Dreaming) → (Evolution)
```

---

## 1. Mathematical Foundation

### The Learning Constant Λ

The intensity of learning is given by:

\[
\Lambda = \frac{\sum(\text{BabySteps} \cdot \pi)}{\text{CoPilot}(\tau)}
\]

- **BabySteps** – vector of small moves (curiosity + noise + audio amplitude)
- **π** – the phase constant (3.14159…)
- **CoPilot(τ)** – steering divisor based on entropy and latency

When Λ is large, the baby mind explores many possibility paths simultaneously.

### Baby‑Step / Giant‑Step (BSGS) Alignment

A standard BSGS algorithm solves discrete logarithms. Here we repurpose it:

- **Baby step** = small, noisy move `b`
- **Giant step** = amplified by CoPilot: `g = pilot * b`

When `|b - g|` falls below the entanglement fidelity threshold, an **evolution event** occurs (ι‑point). This mimics a sudden insight or “aha moment.”

---

## 2. Core Subsystems

| Subsystem | File | Role |
|-----------|------|------|
| **Baby Memory** | `memory.py` | soft, noisy, short‑term storage; imprints with noise, recalls with fuzziness |
| **Color Emotion** | `emotion.py` | maps numeric state to color and reward to emotion words |
| **Curiosity Driver** | `curiosity.py` | generates random novelty pressure between `min` and `max` |
| **Baby Lock** | `babylock.py` | prevents learning > 0.9 by forgetting 40% (eternal infancy) |
| **Sensory Input** | `sense.py` | converts text, RGB color, or numbers into scalar sensations |
| **Inner Voice** | `inner_voice.py` | produces a first‑person monologue string for logging |
| **Dreamer** | `dream.py` | randomly recombines memory with noise (5% chance per step) |
| **Proto‑Self** | `selfmodel.py` | returns a dictionary of current state (learning, curiosity, emotion) |
| **Reward System** | `reward.py` | novelty reward + stagnation penalty; clamped to [-1, 1] |
| **Quantum‑Zinnai Core** | `zinnai_baby_mind.py` | orchestrates everything, loads config, runs the loop |

---

## 3. Data Flow (One Iteration)

1. **Get baby step** – from simulated neural audio amplitude × quantum seed.
2. **Compute giant step** – baby step × pilot.
3. **Curiosity drive** – random uniform [min, max].
4. **Sensory input** – if external text/color is provided, add to curiosity.
5. **Reward** – novelty (delta from previous state) + curiosity alignment – stagnation penalty.
6. **Update learning** – add `|giant - baby|/1000 + reward * learning_rate`; apply Baby Lock.
7. **Color emotion** – map learning value to rainbow color index.
8. **Inner monologue** – generate string.
9. **Dream** – if random < probability, recombine memory.
10. **Proto‑self** – store current snapshot.
11. **Evolution check** – if `|baby - giant| < (1 - bell_ratio)`, trigger evolution and mutate seed.
12. **Update CoPilot** – adjust pilot based on new entropy/latency.
13. **Log Λ** – compute Learning Constant from last 10 baby steps.

---

## 4. Configuration (`config.yaml`)

All parameters are externalised. See `config.yaml` for full list. Key groups:

- **learning** – goal, learning_rate
- **copilot** – base_pi, entropy_init, latency_ms
- **memory** – size, noise
- **curiosity** – min, max
- **dream** – probability
- **reward** – decay, stuck_threshold
- **audio** – freq_low, freq_high, amplitude_range
- **quantum** – bell_state_ratio
- **sensing** – text_enabled, color_enabled
- **logging** – verbose, print_interval

Changing any value in `config.yaml` and restarting the baby mind will alter its behaviour.

---

## 5. Running the System

### Console demo (interactive chat)
```bash
python examples/demo_console.py
```

### Live telemetry simulation (Azure Kronos style)
```bash
python examples/live_telemetry_sim.py
```

### Web dashboard
```bash
python web/app.py
```
Then open `http://localhost:5000`

### Unit tests
```bash
pytest tests/
```

---

## 6. Design Philosophy

- **Never converge** – the Baby Lock ensures the mind stays in a learning state forever.
- **Noise is fuel** – randomness is not error; it is curiosity and dreaming.
- **Emotion as color** – state is felt, not just computed.
- **Quantum analogy** – CoPilot (πηδ) acts like an operator that rotates the possibility vector.
- **Infant intelligence** – not goal‑driven, but novelty‑driven.

---

## 7. Extending Zinnai

Possible next layers (not yet implemented in core):

- **Multi‑sensory fusion** – combine audio, text, and vision into a single sensation vector.
- **Tiny language generator** – produce proto‑words like “da-da” when reward > threshold.
- **World sandbox** – a simple grid where baby moves toward high‑reward cells.
- **Azure IoT integration** – send Λ, emotion, and reward to Azure IoT Hub.

---

*Last updated: 2026-05-10*
```

---
