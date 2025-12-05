import mysql.connector
from mysql.connector import Error


class LoginSystem:
    def __init__(self):
        self.connection = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rooot123",   # <-- Your password
                database="login"        # <-- Your database
            )

            if self.connection.is_connected():
                print("Successfully connected to MySQL database")

        except Error as e:
            print(f"\n❌ Error connecting to database: {e}")
            self.connection = None   # Make sure connection stays None

    def view_all_users(self):
        if not self.connection or not self.connection.is_connected():
            print("\n❌ Cannot fetch users. Database not connected.")
            return

        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()

            if not users:
                print("\nNo users found in database.")
                return

            print("\n--- Users in Database ---")
            for user in users:
                print(user)

        except Error as e:
            print(f"\n❌ Error fetching users: {e}")

    def show_menu(self):
        while True:
            print("\nMenu:")
            print("1. View all users")
            print("2. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_all_users()

            elif choice == '2':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Try again.")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")


def main():
    login_system = LoginSystem()

    # If DB connection failed, do not continue
    if not login_system.connection or not login_system.connection.is_connected():
        print("\n❌ Program stopped because database connection failed.")
        return

    try:
        login_system.show_menu()
    finally:
        login_system.close_connection()


if __name__ == "__main__":
    main()
