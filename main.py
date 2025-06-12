from db import create_tables
from user import signup, signin

def greeting() -> None:
    print('Welcome to the online shop!')
    print("You can search for products by typing a product name.")

def main() -> None:
    create_tables()

    registration: str = input('Sign up/Sign in (write one): ').strip().lower()

    if registration == 'sign up':
        signup()
    elif registration == 'sign in':
        if not signin():
            return
    else:
        print("Invalid choice")
        return

    greeting()

if __name__ == '__main__':
    main()