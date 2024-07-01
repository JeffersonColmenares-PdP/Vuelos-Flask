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

#----------------TABLA TRADUCCIONES -------------------------------
servicio_2_blueprint.add_url_rule(
    "/nombre-pais-traducciones",
    view_func=controllers.cru_tabla_nombre_pais_traducciones,
    methods=["GET", "POST", "PUT"]
)

#--------------TABLA FRONTERAS ---------------------------------
servicio_2_blueprint.add_url_rule(
    "/fronteras",
    view_func=controllers.cru_tabla_fronteras,
    methods=["GET", "POST", "PUT"]
)


#----------------TABLA UNION PAISES FRONTERAS -------------------------------
servicio_2_blueprint.add_url_rule(
    "/union-pais-fronteras",
    view_func=controllers.cru_union_pais_fronteras,
    methods=["GET", "POST"]
)

servicio_2_blueprint.add_url_rule(
    "/buscar-pais-frontera",
    view_func=controllers.obtener_buscar_pais_fronteras,
    methods=["GET"]
)
