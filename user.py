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

def signin() -> bool:
    email: str = input('Enter your email: ').strip()
    password: str = input('Enter your password: ').strip()

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM user WHERE email = ? AND password = ?", (email, password))
        user: Optional[tuple] = cur.fetchone()

        if user:
            print(f"Welcome back, {user[0]}!")
            return True
        else:
            print("Invalid email or password")
            return False