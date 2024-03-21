from flask import Flask, request, jsonify
import psycopg2
app = Flask(__name__)
hostname = 'localhost'
database = 'Week2'
username = 'postgres'
password = '12345678'
port = '5432'
conn = None
cur = None
def connect():
    global conn, cur
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port
        )
        cur = conn.cursor()
        return conn
    except Exception as error:
        if cur:
            cur.close()
        if conn:
            conn.close()
def init_table():
    try:
        connect()
        create_table ='''   CREATE TABLE IF NOT EXISTS profile(
                                id int PRIMARY KEY,
                                name varchar(50) NOT NULL,
                                address varchar(100),
                                job varchar(100),
                                phone_number varchar(15))'''
        cur.execute(create_table)

        insert = 'INSERT INTO profile (id, name, address, job, phone_number) VALUES (%s, %s, %s, %s, %s)'
        values = [(1, 'Nguyen', 'Phu Tho', 'Sale', '000000000'),
                  (2, 'Thu', 'Quang Binh', 'Sale', '111111111'),
                  (3, 'Hong', 'Ha Noi', 'Sale', '222222222'),
                  (4, 'Trang', 'Phu Tho', 'Sale', '333333333')]
        for value in values:
            cur.execute(insert, value)
        conn.commit()
        return conn
        # cur.close()
        # conn.close()

    except Exception as error:
        print(str(error))
        if cur:
            cur.close()
        if conn:
            conn.close()
@app.route('/data/profile', methods = ['POST'])
def get_profile():
    try:
        conn = connect()
        cur = conn.cursor()
        init_table()
        name = request.json.get('name')
        res = cur.execute('SELECT * FROM profile WHERE name = %s', (name,))

        res = cur.fetchall()

        return jsonify((res, 200))

    except Exception as error:
        return jsonify({
            'status': 'faild'
            }, 400)
    finally:
        cur.close()



if __name__ == '__main__':
    app.run(debug=True)
