import mysql.connector
import time
def database():
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="tiger")
        c=db.cursor()
        query="CREATE DATABASE Library;"
        c.execute(query)
        db.commit()
    except Exception:
        c.close()
        db.close()
def create():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    cursor.execute("CREATE TABLE Library (ID char(30) primary key,Title char(100),Author char(15),Genre varchar(30),Available varchar(10),Id_of_Borrower varchar(10);")
    db.commit()
    cursor.close()
    db.close()


def intro():
    print("=" * 80)
    print(' '*39,"LIBRARY")
    print(' '*37,"MANAGEMENT")
    print(' '*39,"PROJECT")
    print("=" * 80)
    print()
    time.sleep(5)


def create_record():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        ID= input("Enter ID: ")
        title = input("Enter Title: ")
        author= input("Enter Author: ")
        Genre= input("Enter Genre: ")
        Avail=input('Enter Availability:')
        Idof=input('Enter Id Of Borrower:')
        sql= "INSERT INTO Library(ID,title,author,Genre,Avail,Idof) VALUES (%s,%s,%s,%s,%s,%s)"
        record=(ID,title,author,Genre,Avail,Idof)
        cursor.execute(sql,record)
        db.commit()
        print("Data Entry Successfull")
    except Exception:
        pass
    cursor.close()
    db.close()


def search(title):
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "SELECT * FROM Library WHERE title = %s"
        value = (name,)
        cursor.execute(sql, value)
        record = cursor.fetchone()
        if record is None:
            print("No such record exists")
        else:
            print('ID:', record[0])
            print('Title:', record[1])
            print('Author:', record[2])
            print('Genre:', record[3])
            print('Availibility:', record[4])
            print('ID of Borrower:', record[5])
    except Exception:
        pass
    cursor.close()
    db.close()


def display_all():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Library")
    print(' '*39,"ID,Title,Author,Genre,Availibility,ID of Borrower")
    for record in cursor:
        print(' '*39,record[0], record[1], record[2], record[3],record[4],record[5])
        print('Successfull')


def delete_record(name):
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "DELETE FROM book WHERE name = %s"
        value = (name,)
        cursor.execute(sql, value)
        db.commit()
        if cursor.rowcount == 0:
            print("Record Not Found")
        else:
            print("Data Deleted successfully")
    except Exception:
        pass
    cursor.close()
    db.close()


def modify_record(title):
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "SELECT * FROM book WHERE name = %s"
        value = (name,)
        cursor.execute(sql, value)
        record = cursor.fetchone()
        if record is None:
            print("No such record exists")
        else:
            while True:
                print("1.ID of Borrower")
                print("2.Genre")
                print("3.Availibility")
                print("4.Exit")
                print()
                ch = int(input("Choice: "))
                if ch == 1:
                    new_name = input("ID of Borrower: ")
                    sql = "UPDATE Library SET title= %s WHERE title= %s"
                    values = (new_name,title)
                    cursor.execute(sql, values)
                    db.commit()
                    print('ID of Borrower Updated')
                elif ch == 2:
                    new_genre = input("Enter new Genre: ")
                    sql = "UPDATE Library SET Genre= %s WHERE title= %s"
                    values = (new_genre,title)
                    cursor.execute(sql, values)
                    db.commit()
                    print('Genre Updated')
                elif ch == 3:
                    new_avail = input("Enter new mobile : ")
                    sql = "UPDATE Library SET Availibility= %s WHERE title= %s"
                    values = (new_avail, name)
                    cursor.execute(sql, values)
                    db.commit()
                    print("Availibility Updated")
                elif ch == 4:
                    break
    except Exception:
        pass
    cursor.close()
    db.close()
            

def main():
    intro()
    database()
    create()
    while True:
        print("\nMAIN MENU ")
        print("1. ADD New Book")
        print("2. SEARCH Book")
        print("3. DISPLAY All Books")
        print("4. DELETE Book")
        print("5. MODIFY Book Data")
        print("6. EXIT")
        print()
        ch = int(input("Choice: "))
        if ch == 1:
            create_record()
        elif ch == 2:
            title= input("Enter Title: ")
            search(title)
        elif ch == 3:
            print("Displaying all Records...........")
            time.sleep(5)
            display_all()
        elif ch == 4:
            name = input("Enter Title: ")
            delete_record(name)
        elif ch == 5:
            name = input("Enter Title: ")
            modify_record(name)
        elif ch == 6:
            break



main()

         
      
















            












            
    
