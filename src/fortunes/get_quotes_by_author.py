
from random_fortune import get_fortune_cookie
from getMultipleFortunes import getMultipleFortunes

import re

def parse_fortune_file(file_path):
    quotes_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Split fortunes using '%' as separator
        fortunes = re.split(r'\n%\n', content)
        
        for fortune in fortunes:
            fortune = fortune.strip()
            if not fortune:
                continue  # Skip empty entries
                
            lines = fortune.split('\n')
            if not lines:
                continue
            
            # Get the last line for the author
            last_line = lines[-1].strip()
            
            # Check for author line starting with '~' or dashes
            author_match = re.match(r'^~\s*(.*)$|^[-–—]{1,2}\s*(.*)$', last_line)
            if author_match:
                author = author_match.group(1) or author_match.group(2)
                author = author.strip()
                quote = '\n'.join(lines[:-1]).strip()
                
                # Add quote to the author's list in quotes_dict
                if author:
                    quotes_dict.setdefault(author, []).append(quote)
            else:
                # If no author is found, you can decide to skip or handle differently
                continue
        
    return quotes_dict


def get_quotes_by_author(quotes_dict):
    while True:
        # Ask the user to input the person name that they want quotes from
        author = input("Enter the name of a famous person: ").strip()
        if author in quotes_dict:
            # Ask the user if they want one quote or multiple quotes
            choice = input("Do you want a random quote or multiple quotes? Enter 'one' or 'multiple': ").strip().lower()
            # User only wants one quote
            if choice == 'one':
                quote = get_fortune_cookie()
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
                quotes = getMultipleFortunes(num_quotes)
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