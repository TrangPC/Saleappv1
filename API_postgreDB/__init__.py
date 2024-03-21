from flask import Flask, jsonify, request, SQLALchemy
from sqlalchemy import Column, Integer, String, Boolean
import psycopg2
app = Flask(__name__)
app.secret_key = 'gjla14234&&o2824jfsj##$gjlajlaaqpri'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname:port/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLALchemy(app)

app.route('/data/profile', methods = ['POST'])
def connect():
    pass
class Profile(db.Model):
    id = Column(Integer, nullable=False, autoincrement=True)
    name = Column(String(50))
    address = Column(String(100))
    job = Column(String(100))
    phone_number = Column(String(100))


if __name__ == '__main__':
    app.run(debug=True)





