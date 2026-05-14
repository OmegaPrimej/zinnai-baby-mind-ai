# Zinnai Baby Mind AI – API Reference

## Core Class: `ZinnaiBabyMind`

The main engine that orchestrates all subsystems.

### `__init__()`
Initializes the baby mind with configuration from `config.yaml`. Creates instances of:
- `BabyMemory`
- `Curiosity`
- `ColorEmotion`
- `BabyLock`
- `SensoryInput`
- `InnerVoice`
- `Dreamer`
- `ProtoSelf`
- `RewardSystem`

Also initializes quantum state: entropy, latency, bell_ratio, audio_amp, seed (512.0), and pilot.

### `step(external_input: Optional[str] = None) -> Dict[str, Any]`
Performs one learning iteration.

**Parameters:**
- `external_input` (optional): Text string to feed as sensory input.

**Returns:** Dictionary with keys:
- `iteration` (int)
- `learning` (float, 0..1)
- `baby_step` (float)
- `giant_step` (float)
- `reward` (float, -1..1)
- `color` (str, e.g., "red")
- `emotion` (str, e.g., "joyful (yellow)")
- `inner_monologue` (str)
- `curiosity` (float)
- `entropy` (float)
- `pilot` (float)
- `learning_constant` (float, Λ)
- `evolved` (bool)
- `dream_occurred` (bool)
- `proto_self` (dict)

---

## Subsystem Classes

### `BabyMemory(size: int = None)`
- `imprint(value: float)` – stores value with noise at random slot.
- `recall() -> float` – retrieves random value with fuzziness.
- `get_all() -> np.ndarray` – returns full memory array.

### `Curiosity()`
- `drive() -> float` – returns random value between `curiosity.min` and `curiosity.max` from config.

### `ColorEmotion()`
- `encode(value: float) -> str` – maps 0..1 to ["red","orange","yellow","green","blue","indigo","violet"].
- `from_reward(reward: float) -> str` – returns "joyful (yellow)", "frustrated (gray)", or "curious (green)".

### `BabyLock()`
- `apply(learning: float) -> float` – if learning > 0.9, returns learning * 0.6, else unchanged.

### `SensoryInput()`
- `text(s: str) -> float` – hashed sum mod 100 / 100.
- `color(rgb: tuple) -> float` – (r+g+b)/765.
- `number(x: float) -> float` – tanh(x).
- `audio_spectrum_amplitude(freq_hz: float) -> float` – linear interpolation between `audio.freq_low` and `audio.freq_high`.

### `InnerVoice()`
- `speak(learning: float, emotion: str) -> str` – returns f"[inner] I feel {emotion} and I am learning {learning:.3f}".

### `Dreamer()`
- `dream(memory_array: np.ndarray) -> np.ndarray` – applies random scaling (0.5-1.5) and noise (±0.2).

### `ProtoSelf()`
- `update(learning: float, curiosity: float, emotion: str) -> dict` – returns snapshot with timestamp.

### `RewardSystem(decay: float = None)`
- `compute(current_state: float, curiosity_drive: float) -> float` – returns reward in [-1, 1] based on novelty and stagnation.

---

## Configuration Access

### `Config()` (singleton)
Loads `config.yaml` once. Access any parameter as attribute, e.g.:
```python
cfg = Config()
print(cfg.LEARNING_RATE)
