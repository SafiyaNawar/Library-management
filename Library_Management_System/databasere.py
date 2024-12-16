import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Safiyasql@13",
    database="lib"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS reports(repnum INT, sname TEXT, bnum INT, sid INT, issued DATE, returnd DATE)')


def add_data(repnum,sname,bnum,sid,issued,returnd):
    c.execute('INSERT INTO reports(repnum,sname,bnum,sid,issued,returnd) VALUES (%s,%s,%s,%s,%s,%s)',(repnum,sname,bnum,sid,issued,returnd))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM reports')
    data = c.fetchall()
    return data


def view_only_repnum():
    c.execute('SELECT repnum FROM reports')
    data = c.fetchall()
    return data


def get_repnum(repnum):
    c.execute('SELECT * FROM reports WHERE repnum="{}"'.format(repnum))
    data = c.fetchall()
    return data


def edit_data(nrepnum,nsname,nbnum,nsid,nissued,nreturnd,repnum,sname,bnum,sid,issued,returnd):
    c.execute("UPDATE reports SET repnum=%s, sname=%s, bnum=%s, sid=%s, issued=%s, returnd=%s  WHERE repnum=%s and sname=%s and bnum=%s and sid=%s and issued=%s and returnd=%s ", (nrepnum,nsname,nbnum,nsid,nissued,nreturnd,repnum,sname,bnum,sid,issued,returnd))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(repnum):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM reports WHERE repnum="{}"'.format(repnum))
    mydb.commit()
