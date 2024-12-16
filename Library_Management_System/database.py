import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Safiyasql@13",
    database="lib"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS books(num INT, title TEXT, genre TEXT,des TEXT, author TEXT, publisher TEXT, availability TEXT, copies INT)')


def add_data(num,title,genre,des,author,publisher,availability,copies):
    c.execute('INSERT INTO books(num,title,genre,des,author,publisher,availability,copies) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(num,title,genre,des,author,publisher,availability,copies))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM books')
    data = c.fetchall()
    return data


def view_only_title():
    c.execute('SELECT title FROM books')
    data = c.fetchall()
    return data


def get_title(title):
    c.execute('SELECT * FROM books WHERE title="{}"'.format(title))
    data = c.fetchall()
    return data


def edit_book_data(nnum,ntitle,ngenre,ndes,nauthor,npublisher,navailability,ncopies, num,title,genre,des,author,publisher,availability,copies):
    c.execute("UPDATE books SET num=%s, title=%s, genre=%s, des=%s, author=%s, publisher=%s, availability=%s, copies=%s WHERE num=%s and title=%s and genre=%s and des=%s and author=%s and publisher=%s and availability=%s and copies=%s", (nnum, ntitle, ngenre, ndes, nauthor, npublisher, navailability, ncopies, num, title, genre, des, author, publisher, availability, copies))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(title):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM books WHERE title="{}"'.format(title))
    mydb.commit()
