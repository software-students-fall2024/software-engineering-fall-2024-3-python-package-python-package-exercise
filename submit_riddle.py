import json

def is_valid_riddle(riddle: dict) -> bool:
    required_keys = {"question", "answer", "hint", "difficulty", "topic"}
    if not all(key in riddle for key in required_keys):
        return False
    if not isinstance(riddle["answer"], list):
        return False
    if not isinstance(riddle["difficulty"], int):
        return False
    return True

def is_duplicate_riddle(riddle: dict, riddles: list) -> bool:
    for existing_riddle in riddles:
        if riddle["question"] == existing_riddle["question"]:
            return True
    return False

def submit_riddle(riddle: dict, riddles: list) -> str:
    try:
        if not isinstance(riddle, dict):
            return "Error: Invalid input. Please enter a dictionary for the riddle."
        
        if not is_valid_riddle(riddle):
            return "Error: Riddle format is incorrect. The correct format is: {\"question\": \"...\", \"answer\": [\"...\"], \"hint\": \"...\", \"difficulty\": \"...\", \"topic\": \"...\"}."
        
        if is_duplicate_riddle(riddle, riddles):
            return "Error: This riddle already exists in the library."
        
        riddle["id"] = len(riddles) + 1
        riddles.append(riddle)
        
        with open("riddleLibrary.json", 'w') as file:
            json.dump(riddles, file)
        
        return "Riddle submitted successfully!"
    
    except Exception as e:
        return f"Unexpected error: {e}"