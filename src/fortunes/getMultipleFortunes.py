import random
<<<<<<< HEAD

def getMultipleFortunes(n):
    file_path = 'resource/fortune.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        fortunes = file.read().split('%')
        fortunes = [fortune.strip() for fortune in fortunes if fortune.strip()]
=======
import importlib.resources

def getMultipleFortunes(n):
    # Use importlib.resources to safely access the fortune.txt file
    with importlib.resources.open_text('fortunes', 'fortune.txt') as file:
        fortunes = [fortune.strip() for fortune in file.read().split('%') if fortune.strip()]
>>>>>>> origin/main

    result = []
    for _ in range(n):
        num = random.randint(1, 100)
        fortune = random.choice(fortunes)
        while fortune in result:
            fortune = random.choice(fortunes)
<<<<<<< HEAD
        result.append([fortune, num])       
    
    return result

#Test trial
# result = getMultipleFortunes(5)
# for fortune, num in result:
#     print(f"Fortune: {fortune}\nNumber: {num}\n")



=======
        result.append(f"🔮 Your Fortune: {fortune}\n🍀 Your Lucky Number: {num}")
    
    return result

if __name__ == "__main__":
    result = getMultipleFortunes(5)
    for fortune, num in result:
        print(f"Fortune: {fortune}\nNumber: {num}\n")
>>>>>>> origin/main
