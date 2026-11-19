"""
savings_analyzer
================
A simple Python package for analyzing monthly savings, savings rate,
and progress toward a savings target.
"""

from .core import (
    calculate_savings,
    savings_rate,
    target_progress,
    months_to_target,
)

__version__ = "0.1.0"

__all__ = [
    "calculate_savings",
    "savings_rate",
    "target_progress",
    "months_to_target",
]
