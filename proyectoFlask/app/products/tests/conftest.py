import pytest

from app import create_app
from app.db import create_all, drop_all, db
from app.products.models import Product, Category
from conf.config import TestingConfig

@pytest.fixture
def app():
    app = create_app(config=TestingConfig)
    with app.app_context():
        create_all()
        app.teardown_bkp = app.teardown_appcontext_funcs
        app.teardown_appcontext_funcs = []
        yield app
        drop_all()
    return app

@pytest.fixture
def product(app):
    with app.app_context():
        product = Product(name="fake-product",
                          image="url",
                          price=1,
                          weight=5.5,
                          description="holiiii",
                          refundable=True,
                          category_id=1)
        db.session.add(product)
        db.session.commit()
        return product

@pytest.fixture
def category(app):
    with app.app_context():
        category = Category(name="fake-category")
        db.session.add(category)
        db.session.commit()
        return category

##@pytest.fixture
##def test_client(app):
##    testing_client = app.test_client()
##    ctx = app.app_context()
    
