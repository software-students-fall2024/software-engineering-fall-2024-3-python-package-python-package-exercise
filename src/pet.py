from time import time, sleep


class Pet:
    def __init__(self, name, timeframe):
        self.name = name
        self.isAlive = True
        self.current_time = int(time())
        self.timeframe = timeframe
        self.stats = {
            "health": 100,
            "food": 100,
            "sleep": 100,
            "happiness": 100
        }
        self.rates = {
            "food": (timeframe * 60 // 100),
            "sleep": timeframe * 60 // 100,
            "happiness": timeframe * 60 // 100
        }

    def time_elapsed(self):
        new_time = int(time())
        difference = new_time - self.current_time
        self.current_time = new_time
        return difference

    def update_stats(self):
        difference = self.time_elapsed()
        self.stats["food"] = max(
            0, self.stats["food"] + difference // self.rates["food"])

        self.stats["sleep"] = max(
            0, self.stats["sleep"] - difference // self.rates["sleep"])

        self.stats["happiness"] = max(
            0, self.stats["happiness"] - difference // self.rates["happiness"])

        self.stats["health"] = (
            self.stats["sleep"] + self.stats["food"] + self.stats["happiness"]) // 3

    def status(self):
        self.update_stats()
        parts = []
        for stat, value in self.stats.items():
            parts.append(f"{stat.capitalize()}: {value}")
        result = " | ".join(parts)
        print(result)


def new_pet(name="", timeframe=10):
    print(
        f"Created new pet: {name}.\nTimeframe: {timeframe} minutes.")
    pet = Pet(name, timeframe)
    pet.status()
    return pet


def main():
    pet_name = "Lucy"
    pet = new_pet(pet_name, 2)
    while (pet.stats["health"] > 0):
        pet.status()
        sleep(1)


if __name__ == "__main__":
    main()
