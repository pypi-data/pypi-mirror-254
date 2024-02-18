from __future__ import annotations


def calculate_mean(numbers):
    if len(numbers) == 0:
        return None  # Handle empty list case
    total_sum = sum(numbers)
    mean = total_sum / len(numbers)
    return mean
