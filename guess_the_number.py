import random

def check_number(r: int, g: int):
    if r < g:
        print('Too High')
    else:
        print('Too Low')


if __name__ == '__main__':
    random_number = random.randint(10, 20)

    while True:
        user_guess = int(input("Guess the number: "))

        if user_guess == random_number:
            break
        else:
            check_number(random_number, user_guess)


