from savings_analyzer import calculate_savings, savings_rate, target_progress, months_to_target

savings = calculate_savings(25000, {"Rent": 8000, "Food": 4000})
print("Savings:", savings)

rate = savings_rate(25000, savings)
print("Savings rate:", rate, "%")

progress, remaining = target_progress(10000, 50000)
print("Progress:", progress, "% | Remaining:", remaining)

months = months_to_target(remaining, savings)
print("Months to reach target:", months)
