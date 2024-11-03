#TODO: IMPLEMENT YOUR FUNCTION IN MAIN BELOW

import sys
from fortune_cookie import get_fortune
from eight_ball import get_eight_ball

def error_msg():
    print("To contact the oracle, type:")
    print("fortune_cookie to receive your fortune")
    print("8ball to make a decision")
    print("petting_zoo to feed your pet")
    print("vibe_check to see what's up")


def main():
    if len(sys.argv) < 2:
        error_msg()
        return
    
    command = sys.argv[1].lower()

    if command == "fortune_cookie":
        print(get_fortune())
    elif command == "8ball":
        print(get_eight_ball())
    elif command == "petting_zoo":
        print("not implemented yet")
    elif command == "vibe_check":
        print("not implemented yet")
    else:
        error_msg()

if __name__ == "__main__":
    main()