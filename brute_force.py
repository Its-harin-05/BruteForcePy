import random
import pyautogui
import argparse
import sys


characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
character_list = list(characters)

def get_password_from_user():
    password = pyautogui.password("Enter password:")
    if not password:
        print("No password entered. Exiting.")
        sys.exit(1)
    return password

def brute_force(password):
    guess_password = ''
    attempts = 0
    
    while guess_password != password:
        guess_password = ''.join(random.choices(character_list, k=len(password)))
        attempts += 1
        print(f"Attempt {attempts}: {guess_password}")
        
        if guess_password == password:
            print(f"Password found: {guess_password}")
            break

def main():
    parser = argparse.ArgumentParser(description="Simple Brute Force Password Cracker")
    parser.add_argument('-p', '--password', type=str, help='Password to guess (if not provided, a prompt will appear)')

    args = parser.parse_args()

    if args.password:
        password = args.password
    else:
        password = get_password_from_user()

    brute_force(password)

if __name__ == "__main__":
    main()
