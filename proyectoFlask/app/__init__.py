from flask import Flask
from products.views import prod

app = Flask(__name__)

app.register_blueprint(prod)

@app.route('/')
def index():
    return "Hola mundo"

#@app.route('/tienda')

if __name__ == "__main__":
    app.run(debug=True)
