from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

from saleapp import db, app
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Category(BaseModel):
    __tablename__ = 'category'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__ = 'product'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    # with app.app_context():
        # db.create_all()

    c1 = Category(name = 'Dien thoai')
    c2 = Category(name = 'May tinh bang')
    c3 = Category(name = 'Dong ho thong minh')
    with app.app_context():
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.commit()

    # products = [{
    #     "id": 1,
    #     "name": "iPhone 15 Pro Max",
    #     "description": "Apple, 256GB, RAM: 8Gb, iOS17",
    #     "price": 17000000,
    #     "image": "images/img1.jpg",
    #     "category_id": 1
    # },
    #     {
    #         "id": 2,
    #         "name": "iPad Pro 2020",
    #         "description": "Apple, 128GB, RAM: 6Gb",
    #         "price": 37000000,
    #         "image": "images/img2.jpg",
    #         "category_id": 2
    #     },
    #     {
    #         "id": 3,
    #         "name": "Samsung Galaxy S24",
    #         "description": "Samsung, 256GB, 5G, RAM: 8GB",
    #         "price": 24000000,
    #         "image": "images/img3.jpg",
    #         "category_id": 1
    #     }]
    # with app.app_context():
    #     for p in products:
    #         pro = Product(name=p['name'], price=p['price'], image=p['image'], description=p['description'],
    #                   category_id=p['category_id'])
    #         db.session.add(pro)
    #     db.session.commit()
