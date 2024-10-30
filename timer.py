import time
import random

def timer(countdown_time):
    if random.choice([True, False]):
        stop_time = random.randint(1, countdown_time - 1)
        for remaining in range(countdown_time, stop_time, -1):
            print(f"Time left: {remaining} seconds")
            time.sleep(random.randint(1, 5))
        print("Done!")
    else:
        for remaining in range(countdown_time, 0, -1):
            print(f"Time left: {remaining} seconds")
            time.sleep(1)
        print("Done!")