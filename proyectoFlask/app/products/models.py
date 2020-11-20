from db import db, ma
from datetime import datetime

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, default=1)
    description = db.Column(db.String(500), nullable=False)
    refundable = db.Column(db.Boolean, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

def get_all_categories():
    categories = Category.query.all()
    category_schema = CategorySchema()
    categories = [category_schema.dump(category) for category in categories]
    return categories

def get_all_products():
    products = Product.query.all()
    product_schema = ProductSchema()
    products = [product_schema.dump(product) for product in products]
    return products

def create_category(name):
    category = Category(name=name)
    db.session.add(category)

    if d.session.commit():
        return category

    return None

def create_product(name,price,weight,description,refundable,category_id):
    cat = db.session.query.filter(id==category_id).first()
    if cat != None:
        prodt = Product(name=name,price=price,weight=weight,description=description,
                      refundable=refundable,category_id=cat.id)
        db.session.add(prodt)

    if d.session.commit():
        return prodt

    return None
