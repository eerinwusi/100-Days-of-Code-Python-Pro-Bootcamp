from game_data import data
from art import logo, vs
import random

print(logo)


def format_description(account):
    a_name = account['name']
    a_description = account['description']
    a_country = account['country']
    return f"{a_name}, {a_description}, from {a_country}"


def get_random_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


counter = 0
play_on = True
random_a = random.choice(data)
random_b = random.choice(data)
if random_b == random_a:
    random_b = random.choice(data)
a_follower_count = random_a['follower_count']
b_follower_count = random_b['follower_count']

higher_value = get_random_number(a_follower_count, b_follower_count)

print(f"Compare A: {format_description(random_a)}.")
print(vs)
print(f"Compare B: {format_description(random_b)}")
response = input("Who has more followers? Type 'A' or 'B': ").lower()

while play_on:
    if response == 'a' and higher_value == a_follower_count:
        counter += 1
        print(f"Your current score is {counter}")
        random_new = random.choice(data)
        random_a = random_b
        a_follower_count = random_a['follower_count']
        new_follower_count = random_new['follower_count']
        higher_value = get_random_number(a_follower_count, new_follower_count)
        print(f"Compare A: {format_description(random_a)}.")
        print(vs)
        print(f"Compare B: {format_description(random_new)}")
        response = input("Who has more followers? Type 'A' or 'B': ").lower()
        random_b = random_new
        b_follower_count = new_follower_count
    elif response == 'b' and higher_value == b_follower_count:
        counter += 1
        print(f"Your current score is {counter}")
        random_new = random.choice(data)
        random_a = random_b
        b_follower_count = random_b['follower_count']
        new_follower_count = random_new['follower_count']
        higher_value = get_random_number(a_follower_count, new_follower_count)
        print(f"Compare A: {format_description(random_a)}.")
        print(vs)
        print(f"Compare B: {format_description(random_new)}")
        response = input("Who has more followers? Type 'A' or 'B': ").lower()
        random_b = random_new
        a_follower_count = new_follower_count
        print(b_follower_count)
        print(new_follower_count)
    else:
        print(f"Sorry, That's wrong. Final Score: {counter}")
        play_on = False


