import argparse
from pyexcuses import pyexcuses

def create_argparser():
    parser = argparse.ArgumentParser(
        description="One line excuses for programmers (excuses as a service)"
    )

    parser.add_argument(
        "-c",
        "--category",
        dest="category",
        choices=["neutral", "chuck", "all"],
        default="neutral",
        help="excuse category.",
    )

    parser.add_argument(
        "-l",
        "--language",
        dest="language",
        choices=[
            "en",
            "es",
        ],
        default="en",
        help="excuse language.",
    )

    return parser


def main():
    parser = create_argparser()

    try:
        args = parser.parse_args()
    except argparse.ArgumentError as exc:
        print("Error parsing arguments.")
        parser.error(str(exc.message))
        exit(-1)

    try:
        excuse = pyexcuses.get_excuse(language=args.language, category=args.category)
    except pyexcuses.LanguageNotFoundError:
        print("No such language %s" % args.language)
        exit(-1)
    except pyexcuses.CategoryNotFoundError:
        print("No such category %s" % args.category)
        exit(-1)

    print(excuse)


if __name__ == "__main__":
    main()
