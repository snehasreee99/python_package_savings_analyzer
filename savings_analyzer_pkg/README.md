# savings-analyzer

A simple Python package for analyzing monthly savings, savings rate,
and progress toward a savings target.

## Install

```bash
pip install savings-analyzer
```

## Usage

```python
from savings_analyzer import calculate_savings, savings_rate, target_progress, months_to_target


savings = calculate_savings(income=25000, expenses={"Rent": 8000, "Food": 4000})


rate = savings_rate(income=25000, savings=savings)


progress, remaining = target_progress(current_savings=10000, target=50000)


months = months_to_target(remaining=remaining, monthly_savings=savings)
```

## Functions

- `calculate_savings(income, expenses)` -- expenses can be a dict or a list
- `savings_rate(income, savings)` -- savings as a % of income
- `target_progress(current_savings, target)` -- returns `(percent, remaining)`
- `months_to_target(remaining, monthly_savings)` -- months needed to close the gap

## License

MIT
