import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Safiyasql@13",
    database="lib"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS studs(sid INT, sname TEXT, address TEXT,phone INT, expiry DATE, mem TEXT)')


def add_data(sid,sname,address,phone,expiry,mem):
    c.execute('INSERT INTO studs(sid,sname,address,phone,expiry,mem) VALUES (%s,%s,%s,%s,%s,%s)',(sid,sname,address,phone,expiry,mem))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM studs')
    data = c.fetchall()
    return data


def view_only_sid():
    c.execute('SELECT sid FROM studs')
    data = c.fetchall()
    return data


def get_sid(sid):
    c.execute('SELECT * FROM studs WHERE sid="{}"'.format(sid))
    data = c.fetchall()
    return data


def edit_stud_data(nsid,nsname,naddress,nphone,nexpiry,nmem,sid,sname,address,phone,expiry,mem):
    c.execute("UPDATE studs SET sid=%s, sname=%s, address=%s, phone=%s, expiry=%s, mem=%s WHERE sid=%s and sname=%s and address=%s and phone=%s and expiry=%s and mem=%s ", (nsid,nsname,naddress,nphone,nexpiry,nmem,sid,sname,address,phone,expiry,mem))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(sid):
    c.execute('SET FOREIGN_KEY_CHECKS=0')
    c.execute('DELETE FROM studs WHERE sid="{}"'.format(sid))
    mydb.commit()
