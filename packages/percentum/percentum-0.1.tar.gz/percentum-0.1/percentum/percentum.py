# sand.py
from datetime import datetime, timedelta
from time import sleep
import sys

def calculate_percentage_used():
    current_time = datetime.now().time()
    start_of_day = datetime.strptime('00:00:00', '%H:%M:%S').time()
    time_used_seconds = (datetime.combine(datetime.today(), current_time) - datetime.combine(datetime.today(), start_of_day)).total_seconds()
    total_seconds_in_a_day = 24 * 60 * 60
    percentage_used = (time_used_seconds / total_seconds_in_a_day) * 100
    return percentage_used

def print_progress_bar(percentage):
    bar_length = 50
    filled_length = int(bar_length * percentage / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'Time Used: |{bar}| {percentage:.2f}%', end='\r', flush=True)

def start():
    try:
        while True:
            percentage_used = calculate_percentage_used()
            print_progress_bar(percentage_used)
            sleep(5)

    except KeyboardInterrupt:
        print(percentage_used)
        print("Keyboard interrupt received. Saying goodbye...")
        print("Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    start()
