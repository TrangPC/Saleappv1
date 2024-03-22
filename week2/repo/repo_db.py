from flask import Flask, request, jsonify, Blueprint
import psycopg2, logging


class PostgreDatabase:
    def __init__(self):
        self.postgre_host = 'localhost'
        self.postgre_port = '5432'
        self.db_user = 'postgres'
        self.db_pass = '12345678'
        self.db = 'week2'

    def get_connection(self):
        try:
            conn = psycopg2.connect(self.postgre_host, self.postgre_port, self.db_user, self.db_pass, self.db);
            return conn
        except Exception as error:
            logging.getLogger().info(f"[ERROR] connect refuse: {str(error)}")

    def create_table(self):
        try:
            '''
                CREATE TABLE IF NOT EXISTS profile(
                    id int PRIMARY KEY,
                    name varchar(50) NOT NULL,
                    address varchar(100),
                    job varchar(100),
                    phone_number varchar(15))
            '''
        except Exception as e:
            logging.getLogger().info(f"[ERROR] create table: {str(e)}")

    def get_profile(self, name):
        conn = self.get_connection()
        try:
            cur = conn.cursor()
            res = cur.execute('Select * from profile where name = %s', (name,))
            res = cur.fetchall()
        except Exception as e:
            logging.getLogger().info(f"[ERROR] get info data: {str(e)}")
        finally:
            cur.close()
            conn.close()
