"""
Unit tests for Baby Memory substrate.
Run with: pytest tests/test_memory.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import numpy as np
from zinnai_baby_mind import BabyMemory

def test_imprint_and_recall():
    """Test that imprint stores a value and recall returns something close."""
    mem = BabyMemory(size=8)
    test_value = 0.42
    mem.imprint(test_value)
    recalled = mem.recall()
    
    # Should be within ~20% due to noise
    assert 0.3 < recalled < 0.55

def test_multiple_imprints():
    """Test that multiple imprints don't raise errors."""
    mem = BabyMemory(size=4)
    for i in range(20):
        mem.imprint(i * 0.1)
    # Should still be able to recall without crash
    recalled = mem.recall()
    assert isinstance(recalled, float)

def test_memory_size():
    """Test that memory array has correct size."""
    size = 16
    mem = BabyMemory(size=size)
    assert len(mem.memory) == size

def test_noise_range():
    """Test that imprinted values include noise within bounds."""
    mem = BabyMemory(size=10)
    exact = 1.0
    mem.imprint(exact)
    # Find where it was stored
    for val in mem.memory:
        if val != 0:
            assert 0.9 <= val <= 1.1  # noise is ±0.1
            break
