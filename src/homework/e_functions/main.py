# src/homework/e_functions/main_program.py
from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds

def format_time(epoch_seconds):
    hours = get_hour(epoch_seconds)
    minutes = get_minutes(epoch_seconds)
    seconds = get_seconds(epoch_seconds)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    epoch_seconds = 3800
    formatted_time = format_time(epoch_seconds)
    print(f"Time: {formatted_time}")

