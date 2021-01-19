# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    return user_input_number.isdigit()


def is_between_100_and_999(user_input_number):
    user_number = int(user_input_number)
    if user_number >= 100 and user_number < 1000:
        return True
    return False


def is_duplicated_number(three_digit):
    set_digit = set(three_digit)
    return len(set_digit) != len(three_digit)


def is_validated_number(user_input_number):
    if is_digit(user_input_number):
        if is_between_100_and_999(user_input_number):
            if not is_duplicated_number(user_input_number):
                return True
            return False
        return False
    return False

def get_not_duplicated_three_digit_number():
    import random
    cands = list(filter(lambda x: not is_duplicated_number(str(x)), range(100, 1000)))
    return random.choice(cands)


def get_strikes_or_ball(user_input_number, random_number):
    strikes = 0
    for user, answer in zip(user_input_number, random_number):
        if user == answer:
            strikes += 1
    commons = len(set(user_input_number) & set(random_number))
    balls = commons - strikes
    return [strikes, balls]


def is_yes(one_more_input):
    possible_inputs = ['y', 'yes']
    return one_more_input.lower() in possible_inputs


def is_no(one_more_input):
    possible_inputs = ['n', 'no']
    return one_more_input.lower() in possible_inputs


def main():
    import sys
    print("Play Baseball")
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    while True:
        user_input_number = input("Input guess number : ")
        if is_validated_number(user_input_number):
            strikes, balls = get_strikes_or_ball(user_input_number, random_number)
            print(f"Strikes : {strikes} , Balls : {balls}")
            if strikes == 3:
                while True:
                    ask_again_input = input("You win, one more(Y/N)?")
                    if is_yes(ask_again_input):
                        random_number = str(get_not_duplicated_three_digit_number())
                        print("Random Number is : ", random_number)
                        break
                    elif is_no(ask_again_input):
                        print("Thank you for using this program")
                        print("End of the Game")
                        sys.exit()
                    else:
                        print("Wrong input, Input again")
        else:
            print("Wrong Input, Input again")

if __name__ == "__main__":
    main()
