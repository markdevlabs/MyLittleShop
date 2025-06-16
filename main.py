from db import create_tables
from user import signup, signin, create_product

def greet() -> None:
    print('Welcome to the online shop!')
    print("You can search/create your product/delete your product")


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


    question: str = input('To create new product enter(create new), to exit(exit): ').strip().lower()


    if question == 'create new':
        create_product()

    elif question == 'exit':
        print('Bye!')
    else:
        pass



if __name__ == '__main__':
    main()