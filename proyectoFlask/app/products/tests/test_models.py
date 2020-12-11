from app.products.models import get_product_by_id
from app.products.exceptions import ProductNotFoundError
import pytest

def test_should_get_product_id_when_product_exists_in_db(app, product):
    with app.app_context():
        result = get_product_by_id(product.id)
        print("Metodo realizado")
        assert result["name"] == product.name

def test_should_raise_error_id_when_product_doesnt_exists_in_db(app):
    with pytest.raises(ProductNotFoundError):
        with app.app_context():
            result = get_product_by_id(999)
