import sqlite3
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#conn = sqlite3.connect('phonebook.db')                                         #default, can remove
#cursor = conn.cursor()                                                         #default, can remove

while True:
    try:
        inp = input("Input SQL commands (type 'EXIT' to quit): ").strip()
        if inp.upper() == "EXIT":
            print("Ciao (garden).")
            conn.close()
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
            print("Command executed successfully.")
    except sqlite3.Error as error:
        print(f"An error occurred: {error}")
    except NameError:
        print("No command can be processed without a database. Use 'ATTACH DATABASE <name>'.")


"""
ATTACH DATABASE 'testBase.db';
CREATE TABLE testTable (integer INTEGER PRIMARY KEY, string TEXT, boolean BOOLEAN, date DATE);
INSERT INTO testTable (integer, string, boolean, date) VALUES (1, 'test', 1, '1987-12-04');
SELECT * FROM testTable;
UPDATE testTable SET string = 'updated' WHERE integer = 1;
DELETE FROM testTable WHERE integer = 1;
"""
#man this orange color is ugly
#it IS sensitive, do not forget the ; signs