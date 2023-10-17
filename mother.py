import mysql.connector as m
#Creation of Database
def db_creation():
    try:
        db=m.connect(host='localhost',user='root',password='tiger')
        c=db.cursor()
        query="CREATE DATABASE Library"
        c.execute(query)
        db.commit()
    except Exception:
        c.close()
        db.close()
                
#Admin functions
def cr_admin():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="CRETE TABLE Admin(AdminId varchar(10) primarykey notnull unique,Adminname varchar(20),Password varchar(20)"
        c.execute(query)
        #/db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def in_admin():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="INSERT INTO Admin values('%s','%s','%s')"
        cH='y'
        while cH=='y':
            temp=()
            i=input('AdminId:')
            n=input('Adminname:')
            a=input('Password:')
            temp=(i,n,a)
            c.execute(query,temp)
            db.commit()
            cH=input('Continue......')
    except Exception:
            pass
    c.close()
    db.close()



    
def display_admin():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        c.execute("SELECT * FROM Admin;")
        data=c.fetchall()
        for records in data:
            print(records)
    except Exception:
        print(Exception)
    c.close()
    db.close()
	
def upd_admin():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        boid=input('AdminId:')
        av=input('Password:')
        c.execute("UPDATE Admin set Password=av where AdminId is boid")
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def drop_admin():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        a="delete from Admin where AdminId='%s"
        b=input('AdminId:')
        c.execute(a,b)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()

#Library functions
def cr_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="CREaTE TaBLE Library(BookId varchar(10),Book varchar(20),User varchar(20),Date_Taken date,Return_Date date,Returned varchar(10)"
        c.execute(query)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()

def in_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="INSERT INTO Library values('%s','%s','%s','%s','%s','%s')"
        cH='y'
        while cH=='y':
            temp=()
            i=input('BookId:')
            n=input('Book:')
            f=input('User:')
            j=input('Date Taken:')
            l=input('Return Date:')
            temp=(i,n,f,j,l)
            c.execute(query,temp)
            db.commit()
            cH=input('Continue......')
    except Exception:
            pass
    c.close()
    db.close()
        
def upd_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        boid=input('BookId:')
        av=input('Returned:')
        c.execute("UPDATE Library set Returned=av where BookId is boid")
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
    
def display_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    c.execute("SELECT * FROM Library")
    data=c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()

	
def search_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    a=input('BookId:')
    c.execute("SELECT * FROM Library where BookId=a")
    data=c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()

def clear_lib():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    c.execute("Delete from Library")
    db.commit()
    c.close()
    db.close()
    
#User functions
def tb_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="CREaTE TaBLE User(UserId varchar(10) primarykey notnull unique,Name varchar(20),Book_Taken varchar(20)"
        c.execute(query)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def in_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="INSERT INTO User values('%s','%s','%s')"
        cH='y'
        while cH=='y':
            temp=()
            i=input('UserId:')
            n=input('Name:')
            a=input('Book Taken:')
            temp=(i,n,a)
            c.execute(query,temp)
            db.commit()
            cH=input('Continue......')
    except Exception:
        pass
    c.close()
    db.close()
def upd_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        boid=input('UserId:')
        av=input('Book_Taken:')
        c.execute("UPDATE User set Book_Taken=av where UserId is boid")
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def drop_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        a="delete from User where UserId='%s"
        b=input('UserId:')
        c.execute(a,b)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def display_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    c.execute("SELECT * FROM User")
    data = c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()
	
def search_user():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    a=input('UserId:')
    c.execute("SELECT * FROM User where UserId=a")
    data=c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()

#Book functions
def cr_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="CREaTE TaBLE Library(Id varchar(10) primarykey notnull unique,Book varchar(20),Author varchar(20),Genre varchar(20),Available varchar(10)"
        c.execute(query)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
def in_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        query="INSERT INTO Book values('%s','%s','%s','%s','%s')"
        cH='y'
        while cH=='y':
            temp=()
            i=input('Id:')
            n=input('Book:')
            a=input('Author:')
            g=input('Genre:')
            f=input('Availability:')
            temp=(i,n,a,g,f)
            c.execute(query,temp)
            db.commit()
            cH=input('Continue......')
    except Exception:
        pass
    c.close()
    db.close()
def upd_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        boid=input('Id:')
        av=input('Availability:')
        c.execute("UPDATE Book set Available=av where Id is boid")
        db.commit()
    except Exception:
                pass
    c.close()
    db.close()
def drop_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    try:
        a="delete from Book where Id='%s"
        b=input('Id:')
        c.execute(a,b)
        db.commit()
    except Exception:
        pass
    c.close()
    db.close()
    
def display_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    c.execute("SELECT * FROM Book")
    data=c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()
	
def search_book():
    db=m.connect(host='localhost',user='root',password='tiger',database='Library')
    c=db.cursor()
    a=input('Book:')
    c.execute("SELECT * FROM Book where Book=a")
    data=c.fetchall()
    for records in data:
        print(records)
    c.close()
    db.close()
    
            
             
