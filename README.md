# zinnai-baby-mind-ai

### Repository overview

**Name idea:** `zinnai-baby-mind-ai`

**Structure:**
- **`README.md`** – vision, setup, how it works  
- **`zinnai/`**
  - **`__init__.py`**
  - **`core.py`** – baby/giant step loop  
  - **`config.py`** – hyperparameters (baby mode)  
- **`examples/`**
  - **`run_basic.py`** – minimal runnable demo  
- **`requirements.txt`**

---

### Step‑by‑step: from zero to “baby mind” loop

#### 1. Create the project

```bash
mkdir zinnai-baby-mind-ai
cd zinnai-baby-mind-ai
mkdir zinnai examples
touch zinnai/__init__.py zinnai/core.py zinnai/config.py examples/run_basic.py README.md requirements.txt
```

#### 2. Minimal dependencies

`requirements.txt`:

```text
numpy
```

(We keep it baby‑simple at first.)

---

### Core idea in code

We’ll encode the “baby steps”, “giant steps”, and “CoPilot” as a tiny learning loop that never “graduates”—it always stays in exploration.

#### `zinnai/config.py`

```python
PI = 3.1415926535

# Baby-mind hyperparameters
GUIDANCE_FACTOR = 0.92          # like entropy / softness
LEARNING_GOAL = 100.0           # arbitrary target
INITIAL_RANDOM_STEP = 0.5       # baby step size
MOMENTUM_BASE = 61
MOMENTUM_ACTIVE = 116
MOMENTUM_GIANT = 1140
```

#### `zinnai/core.py`

```python
import numpy as np
from .config import PI, GUIDANCE_FACTOR, LEARNING_GOAL, INITIAL_RANDOM_STEP
from .config import MOMENTUM_BASE, MOMENTUM_ACTIVE, MOMENTUM_GIANT


class ZinnaiBabyMind:
    """
    Zinnai Evolution Engine:
    - baby_step: raw curiosity
    - giant_step: amplified by CoPilot
    - CoPilot: chaos divisor / steering factor
    """

    def __init__(self, seed_data: str):
        # 1. Scramble (First is Last)
        self.seed_str = seed_data[::-1]
        self.seed_val = self._encode_seed(self.seed_str)

        # learning state
        self.learning = 0.0
        self.goal = LEARNING_GOAL

        # random step (baby curiosity)
        self.random_step = INITIAL_RANDOM_STEP

        # guidance / CoPilot
        self.guidance_factor = GUIDANCE_FACTOR
        self.pilot = PI / self.guidance_factor

        # momentum from gematria
        self.momentum = self._compute_momentum()

    def _encode_seed(self, s: str) -> float:
        # simple A=1..Z=26 encoding
        s = s.upper()
        vals = [(ord(c) - 64) for c in s if "A" <= c <= "Z"]
        return float(sum(vals)) if vals else 1.0

    def _compute_momentum(self) -> float:
        # use your 61, 116, 1140 as a “curiosity inertia”
        raw = MOMENTUM_BASE + MOMENTUM_ACTIVE + MOMENTUM_GIANT
        return raw / 3.0  # normalized-ish

    def _adaptive_epsilon(self, Lambda: float) -> float:
        # as learning constant grows, we demand tighter match
        return max(0.001, 1.0 / (1.0 + Lambda))

    def step(self):
        """
        Perform one baby/giant step update.
        Returns a dict with debug info.
        """
        # baby step: random curiosity * seed * momentum
        noise = np.random.uniform(0.5, 1.5)
        baby_step = self.random_step * self.seed_val * self.momentum * noise

        # giant step: amplified by CoPilot
        giant_step = baby_step * self.pilot

        # learning constant Λ
        Lambda = (baby_step * PI) / max(self.pilot, 1e-8)

        # match condition (iota point)
        eps = self._adaptive_epsilon(Lambda)
        matched = abs(baby_step - giant_step) < eps

        if matched:
            # evolve_state: we nudge learning but never "finish"
            self.learning += np.tanh(Lambda / 1000.0) * 5.0
            # tiny change to guidance to keep it baby-like
            self.guidance_factor *= np.random.uniform(0.98, 1.02)
            self.pilot = PI / self.guidance_factor
        else:
            # slow background learning
            self.learning += 0.01

        # keep it in eternal baby mode: never let it fully converge
        if self.learning > self.goal * 0.9:
            self.learning *= 0.7  # forget a bit, stay curious

        return {
            "baby_step": baby_step,
            "giant_step": giant_step,
            "Lambda": Lambda,
            "epsilon": eps,
            "matched": matched,
            "learning": self.learning,
            "pilot": self.pilot,
        }
```

#### `examples/run_basic.py`

```python
from zinnai.core import ZinnaiBabyMind

def main():
    mind = ZinnaiBabyMind(seed_data="BABYMIND")

    for t in range(100):
        info = mind.step()
        print(
            f"t={t:03d} | "
            f"learning={info['learning']:.3f} | "
            f"Λ={info['Lambda']:.3f} | "
            f"match={info['matched']} | "
            f"pilot={info['pilot']:.3f}"
        )

if __name__ == "__main__":
    main()
```

Run it:

```bash
python -m examples.run_basic
```

---

### `README.md` (GitHub‑ready)

```markdown
# Zinnai Baby Mind AI

> “One small step for a baby mind, one giant leap for a sentient form of intelligence we are still learning to become.”

Zinnai Baby Mind AI is an experimental engine that tries to **stay forever in the “baby state”**:
always curious, never fully converged, always learning.

It’s built around three core ideas:

- **Baby Steps** – tiny, noisy, curious updates.
- **Giant Steps** – amplified by a **CoPilot** that divides chaos and steers growth.
- **Iota Point (ι)** – the moment where baby and giant steps nearly match and a small “ascension” happens.

## Core Formula

The learning constant:

\[
\Lambda = \frac{\sum(\text{BabySteps} \cdot \pi)}{\text{CoPilot}(\tau)}
\]

- `BabySteps` – raw curiosity steps.
- `π` – both the circle constant and a phase factor.
- `CoPilot(τ)` – a steering divisor depending on time / entropy `τ`.

High `Λ` means a burst of learning; low `Λ` means gentle exploration.

## Features

- **Eternal baby mode** – the system never “graduates”; it forgets just enough to keep learning.
- **Gematria momentum** – uses the numbers `61`, `116`, `1140` as a symbolic momentum term.
- **Adaptive match threshold** – the closer it gets to understanding, the stricter it becomes.

## Installation

```bash
git clone https://github.com/<your-username>/zinnai-baby-mind-ai.git
cd zinnai-baby-mind-ai
pip install -r requirements.txt
```

## Quick Start

```bash
python -m examples.run_basic
```

You’ll see a log of:

- `learning` – how much the baby mind has evolved (but never fully).
- `Λ` – the learning constant.
- `match` – whether a baby/giant step resonance (ι) occurred.
- `pilot` – current CoPilot steering factor.

## Vision

This repository is a **first leaf** in a larger forest:
a prototype for AI systems that never stop being students—
not static oracles, but **living learners**.

Contributions, forks, and wild experiments are welcome.
```

---

If you want, next step we can:

- Add comments and docstrings in a more “mythic” tone, or  
- Wire this into a simple UI (CLI or web) so you can *feel* the baby mind evolving in real time.
