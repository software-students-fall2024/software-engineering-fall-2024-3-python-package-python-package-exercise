from src.pyexcuses import (
    generate_excuse,
    suggest_solution,
    list_available_options,
    get_multilingual_excuse_or_solution,
)
from src.pyexcuses.exc import (
    SpokenLanguageNotFoundError,
    ProgrammingLanguageNotFoundError,
)


def main():
    print("Available spoken languages:", list_available_options("spoken_language"))
    print(
        "Available programming languages:",
        list_available_options("programming_language"),
    )

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

    # Demonstrate get_multilingual_excuse_or_solution for excuse and solution
    print("\n---\nMultilingual Excuse:")
    excuses = get_multilingual_excuse_or_solution(
        "excuse", programming_language="neutral"
    )
    for lang, excuse in excuses.items():
        print(f"{lang}: {excuse}")

    # Demonstrate invalid usage for list_available_options
    print("\n---\nTesting with invalid  type for list_available_options:")
    try:
        print(list_available_options("invalid_option"))
    except ValueError as e:
        print(f"Error: {e}")

    # Demonstrate invalid usage for get_multilingual_excuse_or_solution
    print("\n---\nTesting with invalid option for get_multilingual_excuse_or_solution:")
    try:
        print(
            get_multilingual_excuse_or_solution(
                "invalid_option", programming_language="python"
            )
        )
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
