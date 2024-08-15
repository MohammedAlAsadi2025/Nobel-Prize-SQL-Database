import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
  	user="me",
  	password="myUserPassword",
  	database ="dswork"
    )

def show_all():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Prize;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()

def insert_data():
    # Gathering user input
    id_val = input("Enter Prize ID (Up to 4 characters)")
    prize_name = input("Enter Prize Name (Up to 50 characters): ")
    description = input("Enter Description (Up to 400 characters), can leave blank): ")
    amount_awarded = input("Enter Amount Awarded (Enter Integers, can leave blank): ")
    date_awarded = input("Enter Date Awarded (DATE format YYYY-MM-DD, can leave blank): ")

    # Constructing the SQL INSERT statement
    sql = "INSERT INTO Prize (Id, prizeName, description, amountAwarded, dateAwarded) VALUES (%s, %s, %s, %s, %s)"

    # Setting default values if left blank
    amount_awarded = int(amount_awarded) if amount_awarded else None
    description = description if description else None
    date_awarded = date_awarded if date_awarded else None

    # Creating a connection and inserting the data
    db = connect_to_db()
    cursor = db.cursor()
    try:
        cursor.execute(sql, (id_val, prize_name, description, amount_awarded, date_awarded))
        db.commit()
        print(f"Prize {id_val} inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()


def delete_by_id():
    target_id = input("Enter the ID to delete: ")
    db = connect_to_db()
    cursor = db.cursor()
    cursor.callproc("DeleteById", [target_id])
    db.commit()
    db.close()

def update_by_id():
    old_id = input("Enter the old ID: ")
    new_id = input("Enter the new ID: ")
    db = connect_to_db()
    cursor = db.cursor()
    cursor.callproc("UpdateById", [old_id, new_id])
    db.commit()
    db.close()

def execute_queries():
    with open("queries.sql", 'r') as file:
        queries = file.read().split(';')
        db = connect_to_db()
        cursor = db.cursor()
        for query in queries:
            if query.strip():
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
        db.close()

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Show all records")
        print("2. Insert new record")
        print("3. Delete record by ID")
        print("4. Update record by ID")
        print("5. Execute all queries")
        print("6. Exit")

        choice = input("> ")

        if choice == "1":
            show_all()
        elif choice == "2":
            insert_data()
        elif choice == "3":
            delete_by_id()
        elif choice == "4":
            update_by_id()
        elif choice == "5":
            execute_queries()
        elif choice == "6":
            break

if __name__ == "__main__":
    main()

