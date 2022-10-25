import sqlite3
from faker import Faker

fake = Faker()


def create_person():
    con = sqlite3.connect("hw2.db")
    cur = con.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS person(
    personid INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR(128) NOT NULL,
    last_name VARCHAR(128) NOT NULL,
    Address VARCHAR(1024) NOT NULL,
    job VARCHAR(128) NOT NULL,
    Age INTEGER NOT NULL
    )
    '''
    cur.execute(sql)
    con.close()


def insert_person(count: int):
    con = sqlite3.connect("hw2.db")
    cur = con.cursor()
    while count > 0:
        fn = fake.name()
        fadr = fake.address()
        fjob = fake.job()
        fage = fake.random_int(18, 45)
        sql = f'''
                INSERT INTO person (first_name, last_name, Address, job, Age) VALUES 
                ('{fn.split(' ')[0]}','{fn.split(' ')[1]}','{fadr}','{fjob}',{fage})
                '''
        cur.execute(sql)
        con.commit()
        count -= 1
    con.close()


def print_person():
    con = sqlite3.connect("hw2.db")
    cur = con.cursor()
    sql = '''
        SELECT * FROM person
        '''
    persons = cur.execute(sql)
    for p in persons:
        print(p)
    con.close()


def delete_person(personid):
    con = sqlite3.connect("hw2.db")
    cur = con.cursor()
    sql = f'''
        DELETE FROM person WHERE personid={personid}
        '''
    cur.execute(sql)
    con.commit()
    con.close()


create_person()
insert_person(21)
print_person()
delete_person(21)
print_person()
