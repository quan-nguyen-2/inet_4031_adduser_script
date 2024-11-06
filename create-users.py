import subprocess

def create_user(username):
    try:
        subprocess.run(['sudo', 'useradd', '-m', username], check=True)
        print(f"User {username} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user {username}.")

with open("create-users.input", "r") as file:
    usernames = file.readlines()

for user in usernames:
    create_user(user.strip())

