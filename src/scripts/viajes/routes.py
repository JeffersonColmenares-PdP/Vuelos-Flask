""" rutas del servicio 2 """

from flask import Blueprint

from . import controllers

#----------------- PRINCIPAL ------------------------------
servicio_2_blueprint = Blueprint(
    "servicio_2_blueprint",
    __name__,
    url_prefix='/servicio-2',
)

#-----------------TABLA PAISES ------------------------------
servicio_2_blueprint.add_url_rule(
    "/consulta-origen",
    view_func=controllers.obtener_origen,
    methods=["GET"]
)

servicio_2_blueprint.add_url_rule(
    "/consulta-destino",
    view_func=controllers.obtener_destino,
    methods=["GET"]
)

servicio_2_blueprint.add_url_rule(
    "/buscar-vuelos-sin-escala",
    view_func=controllers.listado_vuelos_sin_escala,
    methods=["GET"]
)