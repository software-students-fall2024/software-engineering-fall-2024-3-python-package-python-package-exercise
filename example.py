import funky_fortune.main as ff

def main():
    zodiac = ff.zodiac_fortune("Aries")

    lucky_num = ff.lucky_number("Foo Bar")

    cookie = ff.fortune_cookie()

    eight_ball = ff.magic_8ball("Will I ever become rich?")

    print(f"My Zodiac Fortune: {zodiac}")
    print(f"My Lucky Number: {lucky_num}")
    print(f"Fortune Cookie: {cookie}")
    print(f"Eight Ball: \n{eight_ball}")

main()
