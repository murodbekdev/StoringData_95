# from pathlib import Path
# import json
#
# username = input("What is your name? ")
#
# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)  #
# print(f"We'll remember you when you come back, {username}")

# Now let's write a new program that greets a user whose name has already been stored

from pathlib import Path
import json

# path = Path('username.json')
# contents = path.read_text()
# username = json.loads(contents)
#
# print(f"Welcome back, {username}")
def get_stored_username(path):
    '''Get stored username if available.'''
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def new_greet_user(path):
    '''Prompt for a new username.'''
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    # print(f"We'll remember you when you come back, {username}")
    return username
def greet_user():
    '''Greet the user by name'''
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}")
    else:
        username = new_greet_user(path)
        print(f"We'll remember you when you come back, {username}")

greet_user()

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}")

greet_user()
