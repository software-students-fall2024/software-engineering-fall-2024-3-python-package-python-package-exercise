#TODO: IMPLEMENT YOUR FUNCTION IN MAIN BELOW

import sys
from fortune_cookie import get_fortune

def error_msg():
    print("To contact the oracle, type:")
    print("fortune_cookie <mood> to receive your fortune (e.g. optimistic, realistic, unfortunate)")
    print("eight_ball to make a decision")
    print("petting_zoo to feed your pet")
    print("vibe_check to see what's up")


def main():
    if len(sys.argv) == 1:
        error_msg()
        return
    
    command = sys.argv[1].lower()

    if command == "fortune_cookie":
        if len(sys.argv) == 3:
            mood = sys.argv[2].lower()
            print(get_fortune(mood))
        else:
            print("please specify a mood: optimistic, realistic, unfortunate")
            error_msg()
    elif command == "eight_ball":
        print("not implemented yet")
    elif command == "petting_zoo":
        print("not implemented yet")
    elif command == "vibe_check":
        print("not implemented yet")
    else:
        error_msg()

if __name__ == "__main__":
    main()