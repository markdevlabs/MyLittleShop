from db import create_tables
from user import signup, signin, choose, create_product, search_product



def main() -> None:
    create_tables()

    registration: str = input('Sign up/Sign in (write one): ').strip().lower()

    if registration == 'sign up':
        signup()
    elif registration == 'sign in':
        if not signin():
            return
    else:
        print("Invalid choice, try again!")
        main()


    while True:
        choose()



if __name__ == '__main__':
    main()