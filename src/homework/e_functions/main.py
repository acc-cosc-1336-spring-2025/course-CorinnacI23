import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds

def show_time(epoch_seconds):
    hour = get_hour(epoch_seconds)
    minute = get_minutes(epoch_seconds)
    second = get_seconds(epoch_seconds)
    print(f"{hour:02}:{minute:02}:{second:02}")

# Call the function with 3800
show_time(3800)



