import mysql.connector
import time

def database():
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="tiger")
        c=db.cursor()
        query="CREATE DATABASE Library"
        c.execute(query)
        db.commit()
    except Exception:
        c.close()
        db.close()
def create():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE Library (ID varchar(30) primary key NOT NULL,Title varchar(20),
Author varchar(100),Genre varchar(30),Available varchar(10),Id_of_Borrower varchar(10))""")
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
    time.sleep(2)


def create_record():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor =db.cursor()
    try:
        sql= """INSERT INTO Library(ID,Title,Author,Genre,Available,Id_of_Borrower)
VALUES (%s,%s,%s,%s,%s,%s)"""
        ch='y'
        while ch=='y':
            ID= input("Enter ID: ")
            Title = input("Enter Title: ")
            Author= input("Enter Author: ")
            Genre= input("Enter Genre: ")
            Available=input('Availibility:')
            Id_of_Borrower=input('Borrower ID:')
            record=(ID,Title,Author,Genre,Available,Id_of_Borrower)
            cursor.execute(sql,record)
            db.commit()
            print("Data Entry Successfull")
            ch=input('Continue........')
    except Exception:
        cursor.close()
        db.close()


def search(title):
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "SELECT * FROM Library WHERE Title = %s"
        value = (title,)
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
    print("ID",' '*9,'Title',' '*10,'Author',' '*10,'Genre',' '*9,'Availibility',' '*9,"ID of Borrower")
    for record in cursor:
        print('{0:13}{1:17}{2:18}{3:16}{4:23}{5:16}'.format(record[0],record[1],record[2],record[3],record[4],record[5]))
    print('Successfull')




def delete_record(name):
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "DELETE FROM Library WHERE Title = %s"
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
        sql = "SELECT * FROM Library WHERE Title = %s"
        value = (title,)
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
                    sql = "UPDATE Library SET ID_of_Borrower= %s WHERE Title= %s"
                    values = (new_name,title)
                    cursor.execute(sql, values)
                    db.commit()
                    print('ID of Borrower Updated')
                elif ch == 2:
                    new_genre = input("Enter new Genre: ")
                    sql = "UPDATE Library SET Genre= %s WHERE Title= %s"
                    values = (new_genre,title)
                    cursor.execute(sql, values)
                    db.commit()
                    print('Genre Updated')
                elif ch == 3:
                    new_avail = input("Enter Availibility : ")
                    sql = "UPDATE Library SET Available= %s WHERE Title= %s"
                    values = (new_avail,title)
                    cursor.execute(sql, values)
                    db.commit()
                    print("Availibility Updated")
                elif ch == 4:
                    break
    except Exception:
        pass
    cursor.close()
    db.close()
def Bor():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        cursor.execute("CREATE TABLE Borrower(Id_of_Borrower varchar(30),Name varchar(20))")
        db.commit()
    except Exception:
        pass
    cursor.close()
    db.close()

def create_Bor():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor =db.cursor()
    try:
        sql="INSERT INTO Borrower(Id_of_Borrower,Name) VALUES (%s,%s)"
        ch='y'
        while ch=='y':
            BID= input("Enter Borrower ID: ")
            Name = input("Enter Name: ")
            record=(BID,Name)
            cursor.execute(sql,record)
            db.commit()
            print("Data Entry Successfull")
            ch=input('Continue........')
    except Exception:
        pass
    cursor.close()
    db.close()
def display_Bor():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Borrower")
    print("BID",' '*7,'Name',' '*10)
    for record in cursor:
        print('{0:13}{1:17}'.format(record[0],record[1]
                                    ))
    print('Successfull')
def delete_Bor():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        sql = "DELETE FROM Borrower WHERE Id_of_Borrower = %s"
        valu =input('Borrower ID To Delete:')
        value=(valu,)
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

def borr():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    l=input('Borrower ID:')
    o=input('ID of Book to Borrow:')
    try:
        tyy=(o,)
        cursor.execute("select Available from Library where ID=%s",tyy)
        f=cursor.fetchone()
        for i in f:
            oo=i
        if oo=='Yes':
            gy=(l,o)
            cursor.execute("update Library set Available='No',Id_of_Borrower=%s where ID=%s",gy)
            db.commit()
        else:
            print('BooK Does not Exist')
    except Exception:
        pass
    cursor.close()
    db.close()

def ret():
    db = mysql.connector.connect(host="localhost",user="root",password="tiger",database="Library")
    cursor = db.cursor()
    try:
        o=input('ID of Book to Return:')
        sql="UPDATE Library Set Available='Yes',Id_of_Borrower='None' WHERE ID=%s"
        tp=(o,)
        cursor.execute(sql,tp)
        db.commit()
    except Exception:
        pass
    cursor.close()
    db.close()



def main():
    intro()
    database()
    create()
    Bor()
    while True:
        print("\nMAIN MENU ")
        print("1. ADD New Book")
        print("2. SEARCH Book")
        print("3. DISPLAY All Books")
        print("4. DELETE Book")
        print("5. MODIFY Book Data")
        print("6. DISPLAY ALL Borrowers")
        print("7. ADD Borrower")
        print("8. DELETE Borrower")
        print("9. RETURN Book")
        print("10. BORROW Book")
        print("11. EXIT")
        print()
        ch = int(input("Choice: "))
        if ch == 1:
            create_record()
        elif ch == 2:
            title= input("Enter Title: ")
            search(title)
        elif ch == 3:
            print("Displaying all Records...........")
            time.sleep(2)
            display_all()
        elif ch == 4:
            name = input("Enter Title: ")
            delete_record(name)
        elif ch == 5:
            title= input("Enter Title: ")
            modify_record(title)
        elif ch == 6:
            display_Bor()
        elif ch==7:
            create_Bor()
        elif ch==8:
            delete_Bor()
        elif ch==9:
            ret()
        elif ch==10:
            borr()
        elif ch==11:
            break



main()
