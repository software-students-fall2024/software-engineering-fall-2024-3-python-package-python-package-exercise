import random

def getMultipleFortunes(n):
    file_path = 'resource/fortune.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        fortunes = file.read().split('%')
        fortunes = [fortune.strip() for fortune in fortunes if fortune.strip()]

    result = []
    for _ in range(n):
        num = random.randint(1, 100)
        fortune = random.choice(fortunes)
        while fortune in result:
            fortune = random.choice(fortunes)
        result.append([fortune, num])       
    
    return result

result = getMultipleFortunes(5)
for fortune, num in result:
    print(f"Fortune: {fortune}\nNumber: {num}\n")



