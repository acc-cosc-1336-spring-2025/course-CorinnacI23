# src/homework/c_decisions/decisions.py
def get_options_ratio(option, total):
    if total == 0:  # Prevent division by zero
        return 0
    return option / total
# src/homework/c_decisions/decisions.py
def get_faculty_rating(ratio):
    if ratio >= 0.9:
        return 'Excellent'
    elif ratio > 0.8:
        return 'Very Good'
    elif ratio > 0.7:
        return 'Good'
    elif ratio > 0.6:
        return 'Needs Improvement'
    else:
        return 'Unacceptable'
