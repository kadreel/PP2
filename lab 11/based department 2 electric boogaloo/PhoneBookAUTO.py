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
    if phone.isdigit():
        cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Contact added.")
        return
    else:
        print("Invalid input. Phone must be integer")
        return


def view_contacts():
    cursor.execute("SELECT * FROM PhoneBook")
    rows = cursor.fetchall()
    print("\n--- PhoneBook contacts ---")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    print("--------------------------\n")
    return


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
    return


def reset_autoincrement():
    cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='PhoneBook';")
    conn.commit()
    return

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
    if column == 'phone' and new_value.isdigit():
        query = f"UPDATE PhoneBook SET {column} = ? WHERE id = ?"
        cursor.execute(query, (new_value, contact_id))
        conn.commit()
    else:
        print("Invalid input. Phone must be integer")
        return

def search_contacts():
    pattern = input("Enter search pattern: ")
    query = "SELECT * FROM PhoneBook WHERE name LIKE ? OR phone LIKE ?"
    cursor.execute(query, (f"%{pattern}%", f"%{pattern}%"))
    rows = cursor.fetchall()
    if rows:
        print("\n--- Search Results ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        print("----------------------\n")
        return
    else:
        print("No matching contacts found.")
        return

def safe_add():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    if phone.isdigit():
        cursor.execute("SELECT COUNT(*) FROM PhoneBook WHERE name = ?", (name,))
        count = cursor.fetchone()[0]
        if count > 0:
            cursor.execute("UPDATE PhoneBook SET phone = ? WHERE name = ?", (phone, name))
            print(f"Contact already exists, '{name}' updated with new phone number.")
        else:
            cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
            print(f"Contact added.")
        conn.commit()
        return
    else:
        print("Invalid input. Phone must be integer")
        return
    

def mass_add():
    while True:
        name = input("Enter name (EXIT to finish): ").strip()
        if name.lower() == 'exit':
            break
        phone = input("Enter phone: ").strip()
        if phone.isdigit():
            cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
            conn.commit()
            print(f"Contact '{name}' added.")
        else:
            print("Invalid input. Phone must be integer")

def view_contacts_paginated():
    limit = int(input("Enter the number of contacts to display: "))
    offset = int(input("Enter the offset (starting point, 0 = beginning): "))
    query = "SELECT * FROM PhoneBook LIMIT ? OFFSET ?"
    cursor.execute(query, (limit, offset))
    rows = cursor.fetchall()
    if limit != 0:
        print("\n--- PhoneBook contacts (Paginated) ---")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
        print("--------------------------------------\n")
    else:
        print("wdym you want to see 0 contacts? do you hate these people?")

def manual():
    global cursor
    while True:
        try:
            inp = input("Input SQL commands (type 'EXIT' to quit): ").strip()
            if inp.upper() == "EXIT":
                print("Ciao (garden) again!")
                break
            elif inp.upper().startswith("ATTACH DATABASE"):             #create or connect to database
                db_name = inp.split()[-1].strip("'\"").strip(";").strip('\'')
                conn = sqlite3.connect(db_name)
                cursor = conn.cursor()
                print(f"Connected to database: {db_name}")
            elif inp.upper().startswith("SELECT"):                      #loop for output
                cursor.execute(inp)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            else:                                                       #literally anything else
                cursor.execute(inp)
                conn.commit()
                print("Command executed")
        except sqlite3.Error as error:
                print(f"ERROR!: {error}")
        except NameError:
                print("No command can be processed without a database. Use 'ATTACH DATABASE <name>'.")
        

while True:
    while True:
        inp = input("Add (Y/N), Safe Add (S), Mass Add (M), View (V), Select View (L), Delete (D), Edit (E), Pattern (P), Manual Command (MANUAL): ").strip().lower()
        if inp == "y":
            break
        elif inp == "v":
            view_contacts()
        elif inp == "n":
            reset_autoincrement()
            conn.close()
            exit()
        elif inp == "d":
            delete_contact()
            print("omg somebody got D-cked")
        elif inp == "e":
            edit_contact()
            print("omg we just tried to E-d somebody")
        elif inp == "p":
            search_contacts()                           #Patterns
        elif inp == "s":
            safe_add()
        elif inp == "m":                                #Insert many
            mass_add()
        elif inp == "l":
            view_contacts_paginated()                   #Pagination
        elif inp == "manual":
            manual()
        else:
            print("...w-what?")
    add_contact()