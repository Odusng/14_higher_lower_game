import random
from game_data import data
from art import logo
from art import vs

print(logo)

def get_random_celeb():
    return random.choice(data)


def play_game():
    score = 0
    celeb_a = get_random_celeb()
    celeb_b = get_random_celeb()
    while celeb_a == celeb_b:
        celeb_b = get_random_celeb()

    while True:
        print(f"Compare A: {celeb_a['name']}, a {celeb_a['description']} from {celeb_a['country']}")
        print(vs)
        print(f"Compare B: {celeb_b['name']}, a {celeb_b['description']} from {celeb_b['country']}")

        guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if (guess == 'A' and celeb_a['follower_count'] > celeb_b['follower_count']) or \
                (guess == 'B' and celeb_b['follower_count'] > celeb_a['follower_count']):
            score += 1
            print(f"Correct! Your score is now {score}\n")
            celeb_a = celeb_b
            celeb_b = get_random_celeb()
            while celeb_a == celeb_b:
                celeb_b = get_random_celeb()
        else:
            print(f"Wrong! Final score: {score}")
            break

play_game()