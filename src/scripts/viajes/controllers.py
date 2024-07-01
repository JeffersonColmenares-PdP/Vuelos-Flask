""" Controladores del servicio 2 = paises """

# pylint: disable-all

from flask import request
import psycopg2

from .queries import Query

#-----------------TABLA PAISES ------------------------------
def obtener_origen():
    try:
        origen = request.args.get('nombre', type=str)
        origen_up = origen.upper()

        results = Query().buscar_origenes(nombre=origen_up)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def obtener_destino():
    try:
        destino = request.args.get('nombre', type=str)
        destino_up = destino.upper()

        results = Query().buscar_destino(nombre=destino_up)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_espanol():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        
        Query().agregar_pais_espanol(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def actualizar_pais_espanol():
    try:
        entrada = request.json
        if "id_paises" not in entrada:
            return {"msg": "El id_paises es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        
            Query().actualizar_pais_espanol(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se actualizo satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#----------------TABLA TRADUCCIONES -------------------------------
def obtener_tabla_nombre_pais_traducciones():
    try:
        page = request.args.get('page', type=int)
        page_size = request.args.get('page_size', type=int)

        results = Query().buscar_tabla_nombre_pais_traducciones(page=page, page_size=page_size)

    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_traducciones():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        
        Query().agregar_pais_traducciones(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def actualizar_pais_traducciones():
    try:
        entrada = request.json
        if "id_traduccion" not in entrada:
            return {"msg": "El id_traduccion es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:

            Query().actualizar_pais_traducciones(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se actualizo satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_nombre_pais_traducciones():
    if request.method == "GET":
        return obtener_tabla_nombre_pais_traducciones()
    if request.method == "POST":
        return agregar_pais_traducciones()
    if request.method == "PUT":
        return actualizar_pais_traducciones()

#--------------TABLA FRONTERAS ---------------------------------
def obtener_tabla_fronteras():
    try:
        page = request.args.get('page', type=int)
        page_size = request.args.get('page_size', type=int)

        results = Query().buscar_tabla_fronteras(page=page, page_size=page_size)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_fronteras():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:       
        Query().agregar_fronteras(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def actualizar_tabla_fronteras():
    try:
        entrada = request.json
        if "id_frontera" not in entrada:
            return {"msg": "El id_frontera es obligatorio", "codigo": 0, "status": False, "obj": {}}
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:

            Query().actualizar_tabla_fronteras(entrada)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se actualizo satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def cru_tabla_fronteras():
    if request.method == "GET":
        return obtener_tabla_fronteras()
    if request.method == "POST":
        return agregar_fronteras()
    if request.method == "PUT":
        return actualizar_tabla_fronteras()
    

#----------------TABLA UNION PAISES FRONTERAS -------------------------------
def obtener_union_pais_fronteras():
    try:
        page = request.args.get('page', type=int)
        page_size = request.args.get('page_size', type=int)

        results = Query().buscar_union_pais_fronteras(page=page, page_size=page_size)
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def agregar_pais_frontera():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().insertar_frontera_pais(entrada.get("nombre_paises"), entrada.get("nombre_frontera"))
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

def obtener_buscar_pais_fronteras():
    try:
        results = Query().buscar_pais_fronteras()
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }

def cru_union_pais_fronteras():
    if request.method == "GET":
        return obtener_union_pais_fronteras()
    if request.method == "POST":
        return agregar_pais_frontera()

