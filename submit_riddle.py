import json
from read_file import read_file

def is_valid_riddle(riddle: dict) -> bool:
    required_keys = {"question", "answer", "hint", "difficulty", "topic"}
    if not all(key in riddle for key in required_keys):
        return False
    if not isinstance(riddle["answer"], list):
        return False
    if not isinstance(riddle["difficulty"], int):
        return False
    return True

def submit_riddle(riddle) -> str:
    try:
        if not isinstance(riddle, dict):
            return "Error: Invalid input. Please enter a dictionary for the riddle."
        
        if not is_valid_riddle(riddle):
            return "Error: Riddle format is incorrect. The correct format is: {\"question\": \"...\", \"answer\": [\"...\"], \"hint\": \"...\", \"difficulty\": \"...\", \"topic\": \"...\"}."
        
        riddles = read_file("riddleLibrary.json")
        
        if not riddles:
            return "Error: Riddle library is empty or could not be loaded."
        
        riddle["id"] = len(riddles) + 1
        riddles.append(riddle)
        
        with open("riddles.json", 'w') as file:
            json.dump(riddles, file)
        
        return "Riddle submitted successfully!"
    
    except Exception as e:
        return f"Unexpected error: {e}"