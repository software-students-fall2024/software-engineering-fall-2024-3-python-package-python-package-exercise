
from random_fortune import get_fortune_cookie
from getMultipleFortunes import getMultipleFortunes

def get_quotes_by_author(quotes_dict):
    # Display the available authors before prompting the user
    print("\nAvailable authors:")
    for author in sorted(quotes_dict.keys()):
        print(f"- {author}")

    while True:
        # Ask the user to input the person name that they want quotes from
        author = input("\nEnter the name of a famous person: ").strip()
        if author in quotes_dict:
            # Ask the user if they want one quote or multiple quotes
            choice = input("Do you want a random quote or multiple quotes? Enter 'one' or 'multiple': ").strip().lower()
            # User only wants one quote
            if choice == 'one':
                quote = get_fortune_cookie(quotes_dict[author])
                print(f"\n{quote}\n  ~ {author}")
            # User wants multiple quotes
            elif choice == 'multiple':
                while True:
                    try:
                        # Let them choose how many they wants aand make sure they enter some positive integers instead of negative or non-integers.
                        num_quotes = int(input(f"How many quotes do you want from {author}? "))
                        if num_quotes > 0:
                            break
                        else:
                            print("Please enter a positive integer.")
                    except ValueError:
                        print("Please enter a valid integer.")
                quotes = getMultipleFortunes(quotes_dict[author], num_quotes)
                print()
                for q in quotes:
                    print(f"{q}\n  ~ {author}\n")
            else:
                print("Invalid choice. Please enter 'one' or 'multiple'.")
                continue  # Ask again
            break  # Exit the loop after displaying quotes
        # Did not find the person, ask user again
        else:
            print("Person not found. Please choose again.")

if __name__ == "__main__":
    quotes_dict = parse_fortune_file('./src/fortunes/fortune.txt')
    get_quotes_by_author(quotes_dict)