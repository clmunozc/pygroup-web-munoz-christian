from flask import Blueprint, Response, request
from http import HTTPStatus
from products.models import get_all_categories, get_all_products

prod = Blueprint('prod', __name__, url_prefix='/products')

@prod.route('/all', methods=['GET'])
def get_products():
     """
     """
     products_ = get_all_products()
     RESPONSE_BODY['message'] = 'OK'
     RESPONSE_BODY['data'] = products_

     return RESPONSE_BODY, 200

@prod.route('/<name>', methods=['GET'])
def get_products(name):
     stn = "<h1>Bienvenido a productos</h1><br/><br/>"
     stn = stn + "Mostrando sitio del producto {}".format(name)
     return stn

def render_template():
    """ El metodo de render_template se utiliza para usar un archivo
    HTML como plantilla para que el modulo de Views.py de nuestra
    aplicacion Flask pueda llenar los campos dinamicos de nuestra
    plantilla HTML con respecto a la URL solicitada por el cliente.
    Entradas:
    ruta al template HTML,
    campos*= contenidos* solicitado de campos.
    Salidas: Vista HTML de la plantilla con el contenido asignado.
    """
    return None

@prod.route('/categories', methods=['GET'])
def get_categories():
     """
     """
     categories_ = get_all_categories()

     RESPONSE_BODY['message'] = 'OK'
     RESPONSE_BODY['data'] = categories_

     return RESPONSE_BODY, 200

@prod.route('/add-category', methods=['POST'])
def create_category():
     """
     """
     if request.method == "POST":
          data = request.json
          category = create_new_category(data['name'])
          RESPONSE_BODY['message'] = 'Category created.'

          return RESPONSE_BODY, 201

@prod.route('/add-product', methods=['POST'])
def create_product():
     """
     """
     if request.method == "POST":
          data = request.json
          category = create_new_product(data['name'],data['price'],data['weight'],
                                        data['description'],data['refundable'],data['category_id'])
          RESPONSE_BODY['message'] = 'Product created.'

          return RESPONSE_BODY, 201
