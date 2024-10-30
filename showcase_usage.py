from src.pyexcuses import generate_excuse, suggest_solution
from src.pyexcuses.exc import (
    SpokenLanguageNotFoundError,
    ProgrammingLanguageNotFoundError,
)


def main():
    spoken_languages = ["en", "es"]
    programming_languages = ["neutral", "javascript", "python", "matlab", "all"]

    # Demonstrate valid usages
    for spoken_language in spoken_languages:
        for programming_language in programming_languages:
            print(f"---\nExcuse in {spoken_language} for {programming_language}:")
            try:
                excuse = generate_excuse(spoken_language, programming_language)
                print(excuse)
            except (SpokenLanguageNotFoundError, ProgrammingLanguageNotFoundError) as e:
                print(f"Error: {e}")

            print(f"Solution in {spoken_language} for {programming_language}:")
            try:
                solution = suggest_solution(spoken_language, programming_language)
                print(solution)
            except (SpokenLanguageNotFoundError, ProgrammingLanguageNotFoundError) as e:
                print(f"Error: {e}")

    # Demonstrate invalid spoken language
    print("\n---\nTesting with invalid spoken language:")
    try:
        generate_excuse("fr", "python")
    except SpokenLanguageNotFoundError as e:
        print(f"Error: {e}")

    # Demonstrate invalid programming language
    print("\n---\nTesting with invalid programming language:")
    try:
        suggest_solution("en", "ruby")
    except ProgrammingLanguageNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
