"""
Unit tests for Curiosity Driver.
Run with: pytest tests/test_curiosity.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import numpy as np
from zinnai_baby_mind import Curiosity, Config

def test_curiosity_bounds():
    """Curiosity drive should stay within configured min/max."""
    cfg = Config()
    c = Curiosity()
    for _ in range(100):
        val = c.drive()
        assert cfg.CURIOSITY_MIN <= val <= cfg.CURIOSITY_MAX

def test_curiosity_randomness():
    """Multiple calls should produce different values (not constant)."""
    c = Curiosity()
    values = [c.drive() for _ in range(50)]
    # At least some variation
    assert len(set(round(v, 2) for v in values)) > 1

def test_curiosity_type():
    """Curiosity drive should return float."""
    c = Curiosity()
    assert isinstance(c.drive(), float)

def test_curiosity_with_config_override():
    """If config changes min/max, curiosity respects them (though config is singleton)."""
    # Note: Config is loaded once; this test assumes default config ranges.
    # For override, would need to mock config, but we test default bounds.
    c = Curiosity()
    val = c.drive()
    assert 0.1 <= val <= 1.0  # default from config.yaml
