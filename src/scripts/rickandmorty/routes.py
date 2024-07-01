""" rutas del servicio 1=rickandmorty """

from flask import Blueprint

from . import controllers

#----------------- PRINCIPAL ------------------------------
servicio_1_blueprint = Blueprint(
    "servicio_1_blueprint",
    __name__,
    url_prefix='/servicio-1',
)

#---------------TABLA PERSONAJES--------------------------------
servicio_1_blueprint.add_url_rule(
    "/personajes",
    view_func=controllers.cru_tabla_personajes,
    methods=["GET", "POST", "PUT"]
)

#--------------TABLA ESPECIES---------------------------------
servicio_1_blueprint.add_url_rule(
    "/especies",
    view_func=controllers.cru_tabla_especies,
    methods=["GET", "POST", "PUT"]
)

#---------------TABLA UNION PAISES - PERSONAJES--------------------------------
servicio_1_blueprint.add_url_rule(
    "/union-pais-personaje",
    view_func=controllers.cru_union_pais_personaje,
    methods=["GET", "POST"]
)
