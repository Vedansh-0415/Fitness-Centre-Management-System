"""
RAHI FITNESS CENTRE - Management System
Console-based Python + MySQL project.

Run: python main.py
"""

from db_config import get_connection


def pause():
    input("\nPress Enter to continue...")


# ---------- Account handling ----------

def login(conn):
    print("\n--- LOGIN ---")
    user_id = input("Enter your user id: ").strip()
    passwd = input("Enter your password: ").strip()

    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM user_fitness_rahi1 WHERE user_id=%s AND password=%s",
        (user_id, passwd),
    )
    row = cur.fetchone()
    cur.close()

    if row:
        print(f"\nSUCCESSFULLY LOGGED IN. Welcome, {row[0]}!")
        return row[0]
    else:
        print("\nInvalid user id or password.")
        return None


def create_account(conn):
    print("\n--- CREATE ACCOUNT ---")
    user_id = input("Choose your user id: ").strip()
    passwd = input("Create your password: ").strip()
    name = input("Your full name: ").strip()

    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO user_fitness_rahi1 (user_id, password, name) VALUES (%s, %s, %s)",
            (user_id, passwd, name),
        )
        conn.commit()
        print("\nAccount created successfully. You can now log in.")
    except Exception as e:
        print(f"\nCould not create account: {e}")
    finally:
        cur.close()


# ---------- Customer handling ----------

def view_customers(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM custmer")
    rows = cur.fetchall()
    cur.close()

    print(f"\nTotal customers: {len(rows)}")
    for row in rows:
        print(row)


def add_or_update_customer(conn):
    print("\n--- ADD / UPDATE CUSTOMER ---")
    try:
        cust_id = int(input("Customer ID (integer): ").strip())
        name = input("Customer name: ").strip()
        address = input("Customer address: ").strip()
        joined_date = input("Joined date (e.g. 2024-06-01): ").strip()
        amt_paid = int(input("Amount paid: ").strip())
    except ValueError:
        print("\nID and amount must be numbers. Try again.")
        return

    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO custmer (custmer_id, custmer_name, custmer_address, joined_date, amt_paid)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                custmer_name = VALUES(custmer_name),
                custmer_address = VALUES(custmer_address),
                joined_date = VALUES(joined_date),
                amt_paid = VALUES(amt_paid)
            """,
            (cust_id, name, address, joined_date, amt_paid),
        )
        conn.commit()
        print("\nCustomer details saved.")
    except Exception as e:
        print(f"\nCould not save customer: {e}")
    finally:
        cur.close()


# ---------- Gym item handling ----------

def view_items(conn, gym_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM jim_items")
    rows = cur.fetchall()
    cur.close()

    print(f"\nItems in {gym_name}'s gym ({len(rows)} total):")
    for row in rows:
        print(row)


def add_item(conn):
    print("\n--- ADD / UPDATE GYM ITEM ---")
    try:
        object_id = int(input("Item code (integer): ").strip())
        object_name = input("Item name: ").strip()
        date_purchased = input("Date of purchase: ").strip()
        repair_date = input("Last repair date (or 'NA'): ").strip()
        total_using = int(input("Total people using it: ").strip())
    except ValueError:
        print("\nCode and total people must be numbers. Try again.")
        return

    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO jim_items (object_id, object_name, date_of_parchase, repairing_data, total_people_using)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                object_name = VALUES(object_name),
                date_of_parchase = VALUES(date_of_parchase),
                repairing_data = VALUES(repairing_data),
                total_people_using = VALUES(total_people_using)
            """,
            (object_id, object_name, date_purchased, repair_date, total_using),
        )
        conn.commit()
        print("\nItem saved.")
    except Exception as e:
        print(f"\nCould not save item: {e}")
    finally:
        cur.close()


# ---------- Menus ----------

def logged_in_menu(conn, name):
    while True:
        print(f"\n===== WELCOME {name.upper()} - RAHI FITNESS CENTRE =====")
        print("1. View customer details")
        print("2. Add / update customer details")
        print("3. View gym items")
        print("4. Add / update gym item")
        print("5. Logout")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_customers(conn)
        elif choice == "2":
            add_or_update_customer(conn)
        elif choice == "3":
            view_items(conn, name)
        elif choice == "4":
            add_item(conn)
        elif choice == "5":
            print("\nLogged out.")
            break
        else:
            print("\nInvalid choice.")
        pause()


def main():
    conn = get_connection()
    print("Connected to database.")

    while True:
        print("\n===== WELCOME TO RAHI FITNESS CENTRE =====")
        print("1. Login")
        print("2. Create new account")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = login(conn)
            if name:
                logged_in_menu(conn, name)
        elif choice == "2":
            create_account(conn)
        elif choice == "3":
            print("\nVisit again. Thank you!")
            break
        else:
            print("\nInvalid choice.")

    conn.close()


if __name__ == "__main__":
    main()
