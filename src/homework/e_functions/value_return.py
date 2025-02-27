# src/homework/e_functions/value_return.py

def get_hour(epoch_seconds):
    """Return the hour from epoch_seconds."""
    return epoch_seconds // 3600

def get_minutes(epoch_seconds):
    """Return the minutes from epoch_seconds."""
    return (epoch_seconds % 3600) // 60

def get_seconds(epoch_seconds):
    """Return the seconds from epoch_seconds."""
    return epoch_seconds % 60
