from flask import Flask, request, jsonify
import psycopg2
app = Flask(__name__)
hostname = 'localhost'
database = 'Week2'
username = 'postgres'
password = '12345678'
port = '5432'
def connect():
    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = password,
            port = port
        )
        cur = conn.cursor()
        create_table ='''   CREATE TABLE IF NOT EXISTS profile(
                                id int PRIMARY KEY,
                                name varchar(50) NOT NULL,
                                address varchar(100),
                                job varchar(100),
                                phone_number varchar(15))'''
        cur.execute(create_table)
        conn.commit()
        return conn
    except Exception as error:
        print(str(error))
        cur.close()
        conn.close()
@app.route('/data/profile', methods = ['POST'])
def get_profile():
    try:
        cur = connect().cursor()

        name = request.json.get('name')
        cur.execute("SELECT * FROM profile WHERE name = %s;", (name,))
        profile_data = cur.fetchone()
        return jsonify(
            profile_data
            , 200)

    except Exception as error:
        return jsonify({
            'status': 'faild'
            }, 400)



if __name__ == '__main__':
    app.run(debug=True)

