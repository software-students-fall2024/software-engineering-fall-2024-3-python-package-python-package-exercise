from time import time, sleep
from .names import generate_name
from .constants import DEFAULT_TIMEFRAME, MAX_STAT_VALUE


class Pet:
    def __init__(self, name=None, timeframe=DEFAULT_TIMEFRAME, immortal: bool = False):

        self.name = name if isinstance(name, str) else generate_name()
        self.immortal = immortal if isinstance(immortal, bool) else False
        self.timeframe = timeframe if isinstance(
            timeframe, (int, float)) and timeframe >= 1 else DEFAULT_TIMEFRAME

        self.current_time = int(time())

        self.stats = {
            "health": MAX_STAT_VALUE,
            "food": MAX_STAT_VALUE,
            "sleep": MAX_STAT_VALUE,
            "happiness": MAX_STAT_VALUE
        }
        self.rates = {
            "food": (self.timeframe * 60) // MAX_STAT_VALUE,
            "sleep": (self.timeframe * 60) // MAX_STAT_VALUE,
            "happiness": (self.timeframe * 60) // MAX_STAT_VALUE
        }

    # Returns the time since this function was last called
    def time_elapsed(self):
        new_time = int(time())
        difference = new_time - self.current_time
        self.current_time = new_time
        return difference

    # Decrement pet's stats based on the time passed
    def update_stats(self):
        difference = self.time_elapsed()
        for stat in ["food", "sleep", "happiness"]:
            if self.rates[stat] != 0:
                self.stats[stat] = max(
                    0, self.stats[stat] - difference // self.rates[stat])
            else:
                self.stats[stat] = max(0, self.stats[stat])

        self.stats["health"] = (
            self.stats["sleep"] + self.stats["food"] + self.stats["happiness"]) // 3

    # Print the pet's current stats
    def status(self):
        self.update_stats()
        parts = []
        for stat, value in self.stats.items():
            parts.append(f"{stat.capitalize()}: {value}")
        result = " | ".join(parts)
        print(result)


# Wrapper to make new pet object
def new_pet(name=None, timeframe=None, immortal=False):

    if not isinstance(name, str):
        name = generate_name()
        print(f"Created new pet with random name: {name}.")

    else:
        print(f"Created new pet: {name}.")

    if not timeframe or timeframe < 1 or not isinstance(timeframe, (int, float)):
        timeframe = DEFAULT_TIMEFRAME
        print(f"Timeframe: {timeframe} minutes (default).")

    elif not isinstance(timeframe, (int, float)):
        print(
            f"Invalid timeframe. Timeframe defaulted to {timeframe} minutes.")

    else:
        print(f"Timeframe: {timeframe} minutes.")

    if immortal:
        print("Immortality: On")

    pet = Pet(name, timeframe, immortal)
    return pet


def main():
    pet = new_pet(timeframe=-1)
    while (pet.stats["health"] > 0):
        sleep(1)
        pet.status()


if __name__ == "__main__":
    main()
