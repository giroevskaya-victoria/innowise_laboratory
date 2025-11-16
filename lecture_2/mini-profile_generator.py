def generate_profile(age):
    if age >= 20:
        return "Adult"
    elif age >= 13:
        return "Teenager"
    else:
        return "Child"


def hobbies_output(arr):
    if not arr:
        print("You didn't mention any hobbies")
    else:
        print(f"Favorite hobbies ({len(arr)}):")
        for i in arr:
            print(f"- {i}")


print('Hello user!')
user_name = input("What's your full name? ")
birth_year_str = input(f"Okay {user_name}. Now let's input your birth year: ")
birth_year = int(birth_year_str)

current_age = 2025 - birth_year

print("Now let's figure out what are your hobbies:)")
hobbies = []
is_stop = True
while is_stop:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby == 'stop':
        is_stop = False
    else:
        hobbies.append(hobby)

life_stage = generate_profile(current_age)

user_profile = {"name": user_name, 'age': current_age, 'stage': life_stage, 'hobbies': hobbies}

print('-' * 15)
print('Profile Summary')
print('-' * 15)

print(f'Your name: {user_profile["name"]}')
print(f"Your age: {user_profile['age']}")
print(f"Your life stage: {user_profile['stage']}")
hobbies_output(user_profile['hobbies'])
