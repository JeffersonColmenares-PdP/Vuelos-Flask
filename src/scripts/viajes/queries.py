""" Queries del servicio 2 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_origenes(self, nombre:str):
        
        query = f"""
            SELECT DISTINCT(Origen) FROM tbl_vuelos
            WHERE Origen LIKE '%{nombre}%'
            ORDER BY Origen ASC;
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                # almacenar como json
                objeto_origen = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                return objeto_origen
            
    def buscar_destino(self, nombre:str):
        
        query = f"""
            SELECT DISTINCT(destino) FROM tbl_vuelos
            WHERE destino LIKE '%{nombre}%'
            ORDER BY destino ASC;
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                # almacenar como json
                objeto_destino = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                return objeto_destino

    def buscar_vuelos_sin_escala(self, nom_origen: str, nom_destino: str):
        query = f"""
            SELECT *
            FROM tbl_vuelos
            WHERE origen = '{nom_origen}' AND destino = '{nom_destino}'
            ORDER BY duracion ASC;
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                # almacenar como json
                objeto_origen = [
                    {columnas[index]: item if not isinstance(item, time) else item.strftime("%H:%M:%S") 
                    for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                return objeto_origen

    def validacion_vuelos_con_escala(self, nom_origen: str, nom_destino: str):
        vuelos_finales = []
        # Buscar vuelos intermedios desde el origen
        query = f"""
            SELECT DISTINCT(destino)
            FROM tbl_vuelos
            WHERE origen = '{nom_origen}';
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                vuelos_intermedios = [
                    {columnas[index]: item if not isinstance(item, time) else item.strftime("%H:%M:%S")
                    for index, item in enumerate(tupla)}
                    for tupla in response
                ]
        ciudad_destino_intermedio = vuelos_intermedios
        # Buscar las ciudades origen que van al destino
        for destino_intermedio in ciudad_destino_intermedio:
            query_final = f"""
                SELECT DISTINCT(origen)
                FROM tbl_vuelos
                WHERE origen = '{destino_intermedio["destino"]}' AND destino = '{nom_destino}';
            """
            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query_final)
                    response_final = cursor.fetchall()
                    columnas = [columna.name for columna in cursor.description or []]
                    vuelos_finales.extend([
                        {columnas[index]: item if not isinstance(item, time) else item.strftime("%H:%M:%S") 
                        for index, item in enumerate(tupla)}
                        for tupla in response_final
                    ])
        return vuelos_finales


