import psycopg2
from psycopg2 import sql


def connect():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="kali",
        host="localhost",
        port="5432"
    )
    return conn


connection = connect()


def make_request(request: str):
    try:
        cursor = connection.cursor()

        cursor.execute(request)
        
        connection.commit()
    except Exception as e:
        print(e)



CREATE_TABLE = """

    CREATE TABLE IF NOT EXISTS STUDENTS (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        matricule INTEGER,
        programme VARCHAR(100)
    )

"""

INSERT_STUDENT = """
    INSERT INTO STUDENTS (name, matricule, programme) VALUES ('John Doe', 123456, 'Computer Science')
"""

if __name__ == "__main__":
    make_request()
    connection.close()



