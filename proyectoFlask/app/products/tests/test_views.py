def test_should_return_status_ok_when_requesting_categories(app,test_client):
    with app.app_context():
        result = test_client.get('/products/categories')
        assert result.status.code == 200

def test_should_return_status_not_found_when_requesting_categories(app,test_client):
    with app.app_context():
        result = test_client.get('/products/categories')
        assert result.status.code == 500
