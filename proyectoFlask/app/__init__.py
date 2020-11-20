from flask import Flask
from db import db, ma
from products.views import prod
from config import DevelopmentConfig

ACTIVE_ENDPOINTS = [('/products', prod)]

def create_app(config=DevelopmentConfig):

    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)    
    
    return app

#@app.route('/tienda')

if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()
