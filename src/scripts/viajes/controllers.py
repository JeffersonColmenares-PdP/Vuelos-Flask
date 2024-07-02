""" Controladores del servicio 2 = paises """

# pylint: disable-all

from flask import request
import psycopg2

from datetime import datetime, timedelta
from .queries import Query

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

def listado_vuelos_sin_escala():
    try:
        # Intentamos obtener los datos de origen y destino de una solicitud (request)
        origen = request.args.get('origen', type=str)
        destino = request.args.get('destino', type=str)
        
        # Convertimos los nombres de origen y destino a mayúsculas
        origen_up = origen.upper()
        destino_up = destino.upper()
        
        # Creamos dos listas vacías para almacenar los vuelos intermedios y finales
        vuelos_intermedios = []
        vuelos_finales = []
        
        # Buscamos vuelos directos entre el origen y el destino
        results = Query().buscar_vuelos_sin_escala(nom_origen=origen_up, nom_destino=destino_up)
        
        # Si no encontramos vuelos directos, buscamos vuelos con escala
        if results == []:
            results = Query().validacion_vuelos_con_escala(nom_origen=origen_up, nom_destino=destino_up)
            
            # Si encontramos vuelos con escala, procedemos a buscar los vuelos intermedios y finales
            if results != []:
                for result in results:
                    # Buscamos vuelos entre el origen y la escala intermedia
                    intermedio = Query().buscar_vuelos_sin_escala(nom_origen=origen_up, nom_destino=result["origen"])
                    vuelos_intermedios.extend(intermedio)  # Agregamos los vuelos intermedios a la lista
                
                    # Buscamos vuelos entre la escala intermedia y el destino
                    final = Query().buscar_vuelos_sin_escala(nom_origen=result["origen"], nom_destino=destino_up)
                    vuelos_finales.extend(final)  # Agregamos los vuelos finales a la lista
                
                # Creamos un objeto que contiene las listas de vuelos intermedios y finales
                obj = {
                    "vuelos_intermedios": vuelos_intermedios,
                    "vuelos_finales": vuelos_finales
                }
                
                # Extraemos las listas de vuelos intermedios y finales del objeto
                vuelos_intermedios = obj['vuelos_intermedios']
                vuelos_finales = obj['vuelos_finales']
                
                # Creamos una lista vacía para almacenar las combinaciones de vuelos
                combinaciones = []
                
                # Iteramos sobre cada vuelo intermedio para buscar vuelos finales válidos
                for vuelo_intermedio in vuelos_intermedios:
                    # Obtenemos la hora de salida del vuelo intermedio y la convertimos a formato datetime
                    hora_intermedia_str = vuelo_intermedio["hora"]
                    hora_intermedia_dt = datetime.strptime(hora_intermedia_str, "%H:%M:%S")
                    
                    # Calculamos la duración del vuelo intermedio y la sumamos a la hora de llegada estimada
                    duracion_intermedia_td = timedelta(hours=int(vuelo_intermedio["duracion"].split(':')[0]), minutes=int(vuelo_intermedio["duracion"].split(':')[1]))
                    llegada_intermedia_dt = hora_intermedia_dt + duracion_intermedia_td
                    
                    # Filtramos los vuelos finales válidos que salen después de la llegada del vuelo intermedio
                    vuelos_finales_validos = []
                    for vuelo_final in vuelos_finales:
                        if vuelo_intermedio["destino"] == vuelo_final["origen"]:
                            # Convertimos la hora de salida del vuelo final a formato datetime
                            hora_vuelo_final = datetime.strptime(vuelo_final["hora"], "%H:%M:%S")
                            
                            # Si la hora de salida del vuelo final es posterior a la llegada del vuelo intermedio, lo agregamos a los vuelos finales válidos
                            if hora_vuelo_final > llegada_intermedia_dt:
                                vuelos_finales_validos.append(vuelo_final)
                    
                    # Ordenamos los vuelos finales válidos por hora de salida y seleccionamos el siguiente vuelo más cercano
                    vuelos_finales_validos.sort(key=lambda x: datetime.strptime(x["hora"], "%H:%M:%S"))
                    if vuelos_finales_validos:
                        vuelo_final_seleccionado = vuelos_finales_validos[0]
                        
                        # Calculamos la duración del vuelo final
                        duracion_final_td = timedelta(hours=int(vuelo_final_seleccionado["duracion"].split(':')[0]), minutes=int(vuelo_final_seleccionado["duracion"].split(':')[1]))
                        
                        # Calculamos la duración total del trayecto, sumando la diferencia entre la salida del primer vuelo y la salida del segundo vuelo, y la duración del segundo vuelo
                        tiempo_espera_td = datetime.strptime(vuelo_final_seleccionado["hora"], "%H:%M:%S") - hora_intermedia_dt
                        duracion_total_td = tiempo_espera_td + duracion_final_td
                        
                        # Agregamos la combinación de vuelos a la lista de combinaciones
                        combinaciones.append({
                            "origen": vuelo_intermedio["origen"],
                            "destino": vuelo_final_seleccionado["destino"],
                            "ciudad_intermedia": vuelo_intermedio["destino"],
                            "hora_ciudad_intermedia": vuelo_intermedio["hora"],
                            "duracion_ciudad_intermedia": vuelo_intermedio["duracion"],
                            "precio_ciudad_intermedia": vuelo_intermedio["precio"],
                            "hora_ciudad_destino": vuelo_final_seleccionado["hora"],
                            "duracion_ciudad_destino": vuelo_final_seleccionado["duracion"],
                            "precio_ciudad_destino": vuelo_final_seleccionado["precio"],
                            "total_vuelo": vuelo_intermedio["precio"] + vuelo_final_seleccionado["precio"],
                            "duracion_total": str(duracion_total_td)
                        })
                
                # Asignamos las combinaciones encontradas a la variable results
                results = combinaciones
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
