import random
import importlib.resources

def getMultipleFortunes(n):
    # Use importlib.resources to safely access the fortune.txt file
    with importlib.resources.open_text('fortunes', 'fortune.txt') as file:
        fortunes = [fortune.strip() for fortune in file.read().split('%') if fortune.strip()]

    result = []
    for _ in range(n):
        num = random.randint(1, 100)
        fortune = random.choice(fortunes)
        while fortune in result:
            fortune = random.choice(fortunes)
        result.append([fortune, num])       
    
    return result

if __name__ == "__main__":
    result = getMultipleFortunes(5)
    for fortune, num in result:
        print(f"Fortune: {fortune}\nNumber: {num}\n")
