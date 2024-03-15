from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from saleapp import db
from datetime import datetime
class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
class Category(BaseModel):
    __tablename__ = 'category'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable = False)
    products = relationship('Product', backref = 'category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    description = Column(String(55))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    db.create_all()

    c1 = Category(name = 'Dien thoai')
    c2 = Category(name = 'May tinh bang')
    c3 = Category(name = 'Dong ho thong minh')
    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.commit()
