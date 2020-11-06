from flask import Blueprint

prod = Blueprint('prod', __name__, url_prefix='/products')

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
