import riddle_handler
print(dir(riddle_handler))

def main():
    # Example 1: Generate a riddle of difficulty level 2
    print("Example 1: Generate a Riddle")
    difficulty_level = 2
    riddle = riddle_handler.generate_riddle(difficulty_level)
    print(f"Here's your riddle (Difficulty {difficulty_level}): {riddle}")
    
    # Assume riddle ID for example purposes
    riddle_id = 5
    
    # Example 2: Check the answer to a riddle
    print("\nExample 2: Check Answer to a Riddle")
    user_answer = 'shadow'  # Example answer; replace with user input in a real application
    result = riddle_handler.check_answer(riddle_id, user_answer)
    print(f"Result for riddle ID {riddle_id} with answer '{user_answer}': {result}")
    
    # Example 3: Submit a custom riddle to the library
    print("\nExample 3: Submit a Custom Riddle")
    custom_riddle = {
        "question": "I speak without a mouth and hear without ears. What am I?",
        "answer": ["echo"],
        "hint": "You can hear me but cannot see me.",
        "difficulty": 2,
        "topic": "Mystery"
    }
    submission_response = riddle_handler.submit_riddle(custom_riddle)
    print(f"Riddle submission response: {submission_response}")
    
    # Example 4: Provide a hint for a riddle
    print("\nExample 4: Get a Hint for a Riddle")
    hint = riddle_handler.provide_hint(riddle_id)
    print(f"Hint for riddle ID {riddle_id}: {hint}")

if __name__ == "__main__":
    main()
