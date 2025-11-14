from sqlalchemy import Integer, String, Column, Boolean, Text, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from eapp import app, db


class BaseModel(db.Model):
    __abstract__ = True #Lệnh này dùng để ngăn class BaseModel này tạo bảng vì có thuộc tính Column ở dưới
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)

class Category(BaseModel):
    name = Column(String(50), unique=True)
    products = relationship("Product", backref="category", lazy=True)
    '''
    Ở Product có lk khóa ngoại với Category thì ở trên Category cũng phải có dòng lệnh thể hiện mqh với
    Product để hệ thống biết.
    ---
    Tham số "Product" là dùng để chỉ cho hệ thống là class Category có mqh với class Product ở dưới, và
    phải bỏ trong dấu nháy đôi vì lệnh đang ở Category mà Product lại ở dưới Category nên hệ thống sẽ ko
    biết Product là gì nếu ko để dấu nháy đôi, để dấu nháy đôi để khi chạy hệ thống sẽ tìm class có tên 
    tương tự trong dấu nháy để thiết lập mqh nếu như class đó được nêu sau class hiện tại đang chạy lệnh đó.
    ---
    Thuộc tính backref="category" dùng để chỉ category là khóa ngoại mà class Product ở dưới lk tới hoặc có
    thể hiểu đó là biến category_id ở class Product
    ---
    Biến cờ lazy=True giúp tối ưu hóa hệ thống, cải thiện hiệu năng, giúp giảm tiêu tốn tài nguyên, khi nào
    cần truy vấn thì mới truy vấn
    '''
    def __str__(self):
        return self.name

class Product(BaseModel):
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0)
    image = Column(String(200), default="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg")
    category_id = Column(Integer, ForeignKey(Category.id))
    def __str__(self):
        return self.name

products = [{
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "name": "iPhone 7 Plus",
        "description": "Apple, 32GB, RAM: 3GB, iOS13",
        "price": 17000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        "category_id": 1
    }, {
        "name": "iPad Pro 2020",
        "description": "Apple, 128GB, RAM: 6GB",
        "price": 37000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        "category_id": 2
    }, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1}, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1
    }, {
        "name": "Galaxy Note 10 Plus",
        "description": "Samsung, 64GB, RAML: 6GB",
        "price": 24000000,
        "image":
            "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        "category_id": 1}]

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()

        for p in products:
            prod = Product(**p)
            db.session.add(prod)

        db.session.commit()

