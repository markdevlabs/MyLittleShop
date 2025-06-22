from typing import Optional
from db import get_connection


def signup() -> None:
    print("Signing up a new user...")

    name: str = input('Enter your name: ').strip()
    lastname: str = input('Enter your lastname: ').strip()
    age: str = input('Enter your age: ').strip()
    email: str = input('Enter your email: ').strip()
    password: str = input('Enter your password: ').strip()

    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO user (name, lastname, age, email, password)
                VALUES (?, ?, ?, ?, ?)
            """, (name, lastname, age, email, password))
            print('Sign up successfully done!')
        except Exception as e:
            print(f"Error during sign up: {e}")



def choose() -> (None, bool):


    question: str = input('To create new product enter(create new), to exit(exit), to search(write product name): ').strip().lower()


    if question == 'create new':
        create_product()

    elif question == 'exit':
        print('Bye!')
        return False


    elif question == 'search':
        search_product()
    else:
        print('Incorrect command, try again')
        pass

    while True:
        choose()


def signin() -> bool:
    email: str = input('Enter your email: ').strip()
    password: str = input('Enter your password: ').strip()

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
        user: Optional[tuple] = cur.fetchone()

        if user:
            print(f"Welcome back, {user[0]}!")
            choose()
            return True
        else:
            print("Invalid email or password, try again")
            signin()
            return False



def create_product() -> (str, float):
    name: str = str(input('Write your name: ').strip())
    product = str(input('Write product name: ').strip())
    product_price: float = float(input('Write product price: ').strip())
    print('Product successfully created!')


    with get_connection() as conn:
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO seller_info (seller_name, product_name, price)
        VALUES (?, ?, ?)
        """, (name, product, product_price))



def search_product() -> None:
    with get_connection() as conn:
        cur = conn.cursor()

        search: str = input('Write product name: ').strip().lower()

        cur.execute("""SELECT seller_name, product_name, price FROM seller_info
        WHERE product_name = ?""", [search])
        print(cur.fetchall())