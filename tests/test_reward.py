"""
Unit tests for Reward System (Proto-Motivation).
Run with: pytest tests/test_reward.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import numpy as np
from zinnai_baby_mind import RewardSystem, Config

def test_reward_initialization():
    """Test that reward system initializes with no last state."""
    rs = RewardSystem()
    assert rs.last_state is None
    assert rs.stuck_counter == 0

def test_first_compute_returns_zero():
    """First compute() should return 0.0 (no history)."""
    rs = RewardSystem()
    reward = rs.compute(0.5, 0.3)
    assert reward == 0.0
    assert rs.last_state is not None

def test_novelty_reward():
    """Large change should give positive reward."""
    rs = RewardSystem()
    rs.compute(0.2, 0.3)   # first call sets last_state
    reward = rs.compute(0.8, 0.3)  # delta = 0.6 → novelty_reward ~1.0
    # curiosity_alignment = 1.0 - |0.3-0.6| = 0.7; weighted avg ~0.88
    assert reward > 0.5

def test_stagnation_penalty():
    """Repeated small changes should trigger penalty."""
    rs = RewardSystem()
    rs.compute(0.5, 0.3)   # set last_state
    # simulate stuck steps
    for i in range(5):
        reward = rs.compute(0.501, 0.3)  # delta ~0.001 (< threshold)
    # stuck_counter should be >0, penalty applied
    assert rs.stuck_counter >= 3
    # reward should be negative or very low
    assert reward < 0.1

def test_reward_clamping():
    """Reward should be clamped between -1 and 1."""
    rs = RewardSystem()
    rs.compute(0.0, 0.0)
    # force extreme values (won't happen naturally, but test clamp)
    rs.last_state = 1.0
    rs.stuck_counter = 100
    reward = rs.compute(0.0, 0.0)  # delta large positive but penalty huge
    assert -1.0 <= reward <= 1.0

def test_decay_effect():
    """Decay should gradually reduce influence of old state."""
    cfg = Config()
    rs = RewardSystem(decay=0.5)  # fast decay
    rs.compute(1.0, 0.0)
    # after several steps, last_state should approach new value
    for _ in range(10):
        rs.compute(0.0, 0.0)
    # last_state should be closer to 0 than to 1
    assert rs.last_state < 0.5
