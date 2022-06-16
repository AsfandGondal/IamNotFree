import sqlite3

db_name = "employee data management.db"



def drop_table():
    sql = "drop table if exists employee"
    db_conn.execute(sql)
    print("Dropped Table.")


def create_table():
    sql = "create table employee ( id integer, name text, role text, salary integer, address text , qualification text)"
    db_conn.execute(sql)
    print("Created Table.")
def delete_row():
    sql = "delete from employee where id = ?"
    # ask the user for the id that they want to delete
    id = input("Enter the id for the employee that you want to delete:")
    tuple_of_values = (id, )
    db_conn.execute(sql, tuple_of_values)
    db_conn.commit()

def select_all():
        sql = "select * from employee"
        result_set = db_conn.execute(sql)
        for row in result_set:
            print(row)

def insert_row():
    # ask the user for the data that we plan to insert
    # build anything we need
    # execute the sql statement against the DB
    id = input("Enter the id (int):")
    name = input("Enter the name (str):")
    role = input("Enter the role (str):")
    salary = input("Enter the salary (int):")
    address = input("Enter the address (str):")
    qualification = input("Enter the qualification (str):")
    sql = "insert into employee values (?, ?, ?, ?, ?, ?)"
    tuple_of_values = (id, name, role, salary, address, qualification)
    db_conn.execute(sql, tuple_of_values)
    print("Inserted row into table.")
    db_conn.commit()
def select_row():
    # ask the user for the row they would like to select
    id = int(input("Enter the id that you wish to select (int): "))
    # create the sql
    sql = "select * from employee where id = ?"
    # create the tuple

    tuple_of_value = (id, )
    result_set = db_conn.execute(sql, tuple_of_value)

    for row in result_set:
        print(row)

def display_menu():

    print("Here are your menu options:")
    while True:
        print("Enter S to get started and create a fresh DB.")
        print("Enter C to create a new row")
        print("Enter R to insert a new row")
        print("Enter U to update a row")
        print("Enter D to delete  a row")
        print("Enter Q to Quit")
        # add in other print statements for each menu option
        choice = input("Enter your choice: ").upper()
        if choice == "S":
            drop_table()
            create_table()
        elif choice == "C":
            insert_row()
        elif choice == "R":
            select_row()
        elif choice == "U":
            update_row()
        elif choice == "D":
            delete_row()
        elif choice == "Q":
            break
        else:
            print("Invalid choice of", choice)
        select_all() # display what is the DB right now.

def update_row():
    # ask the user to update the row
    id = input("Enter the id that you wish to update (int): ")
    # ask the user for 2 new values for the 2 fields _ role, salary

    role = input("Enter the new role value (str): ")
    salary = float(input("Enter the new salary (str): "))
    # create the sql statement
    sql = "update employee set role = ?, salary = ? where id = ?"

    # create the tuple
    tuple_of_values = (role, salary, id)
    # call the execute
    db_conn.execute(sql, tuple_of_values)
    # commit
    db_conn.commit()
    # print statement
    print("Row updated. ")





db_conn = sqlite3.connect(db_name)
print("connected to DB.")
display_menu()
db_conn.close()