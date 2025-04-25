import sqlite3
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
phone TEXT NOT NULL
)
""")


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()
    print("Contact added.")


def view_contacts():
    cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    print("\n--- PhoneBook contacts ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    print("--------------------------\n")


def delete_contact():
    view_contacts()
    contact_id = int(input("WHO IS DYING?! "))
    cursor.execute("SELECT COUNT(*) FROM PhoneBook WHERE id = ?", (contact_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        print(f"WHO IS THAT!??!?! NO {contact_id}. LEAVE.")
        return
    cursor.execute("DELETE FROM PhoneBook WHERE id = ?", (contact_id,))
    reset_autoincrement()
    conn.commit()


def reset_autoincrement():
    cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='PhoneBook';")
    conn.commit()

def edit_contact():
    view_contacts()
    contact_id = int(input("WHO IS changing?! "))
    cursor.execute("SELECT COUNT(*) FROM PhoneBook WHERE id = ?", (contact_id,))
    count = cursor.fetchone()[0]
    if count == 0:
        print(f"WHO IS THAT!??!?! NO {contact_id}. LEAVE.")
        return
    column = input("WHAT EXACTLY? ").strip().lower()
    if column not in ['name', 'phone']:
        print("WRONG WRONG WRONG")
        return
    new_value = input(f"HOW DOES THEIR {column} CHANNGE?!? ")
    query = f"UPDATE PhoneBook SET {column} = ? WHERE id = ?"
    cursor.execute(query, (new_value, contact_id))
    conn.commit()

def query_contacts():
    print("\n--- Query Contacts ---")
    print("Filter options: ")
    print("1. By Name")
    print("2. By Phone")
    print("3. By Both Name and Phone")
    print("4. View All")
    choice = input("Choose a filter option (1/2/3/4): ").strip()

    if choice == "1":
        name = input("Enter name to search: ").strip()
        cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE ?", (f"%{name}%",))
    elif choice == "2":
        phone = input("Enter phone to search: ").strip()
        cursor.execute("SELECT * FROM PhoneBook WHERE phone LIKE ?", (f"%{phone}%",))
    elif choice == "3":
        name = input("Enter name to search: ").strip()
        phone = input("Enter phone to search: ").strip()
        cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE ? AND phone LIKE ?", (f"%{name}%", f"%{phone}%"))
    elif choice == "4":
        cursor.execute("SELECT * FROM PhoneBook")
    else:
        print("Invalid choice. Returning to main menu.")
        return

    rows = cursor.fetchall()
    print("\n--- Query Results ---")
    if rows:
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("No contacts found.")
    print("----------------------\n")

while True:
    while True:
        inp = input("Add (Y/N), View (V), Filtered query (Q), Delete (D), Edit (E): ").strip().lower()
        if inp == "y":
            break
        elif inp == "v":
            view_contacts()
        elif inp == "n":
            conn.close()
            exit()
        elif inp == "d":
            delete_contact()
            print("omg somebody got D-cked")
        elif inp == "e":
            edit_contact()
            print("omg we just tried to E-d somebody")
        elif inp == "q":
            query_contacts()
        else:
            print("what?")
    add_contact()