import pytarot.truelover as truelover_module
import pytarot.luckyday as luckyday_module
import pytarot.answersofwisdom as answers_of_wisdom_module


def main():
    print("default method")

def get_trueLover():
    line = truelover_module.get_true_lover()
    print(line)

def get_luckyDay():
    line = luckyday_module.get_lucky_day()
    print(line)

def get_answersOfWisdom ():
    line = answers_of_wisdom_module.get_answers_of_wisdom()
    print(line)


if __name__ == "__main__":
    main()
