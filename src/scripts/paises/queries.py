""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_tabla_pais_espanol(self, page:int, page_size: int):
        
        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        # Consulta para obtener el número total de registros
        total_query = "SELECT COUNT(*) FROM tabla_pais_espanol"

        query = f"""
            SELECT * FROM tabla_pais_espanol ORDER BY id_paises ASC
            LIMIT {page_size} OFFSET {offset} 
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(total_query)
                total = cursor.fetchone()[0]
                
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)

                respuesta = {
                    "total": total,
                    "objeto_pais_espanol": objeto_pais_espanol
                }

                return respuesta

    def buscar_tabla_nombre_pais_traducciones(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar
        # Consulta para obtener el número total de registros
        total_query = "SELECT COUNT(*) FROM tabla_nombre_pais_traducciones"

        query = f"""
            SELECT * FROM tabla_nombre_pais_traducciones 
            JOIN tabla_pais_espanol ON tabla_pais_espanol.id_paises = tabla_nombre_pais_traducciones.fk_pais
            ORDER BY id_traduccion ASC
            LIMIT {page_size} OFFSET {offset} 
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(total_query)
                total = cursor.fetchone()[0]

                cursor.execute(query)
                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)
                respuesta = {
                    "total": total,
                    "objeto_pais_espanol": objeto_pais_espanol
                }

                return respuesta

    def buscar_tabla_fronteras(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        # Consulta para obtener el número total de registros
        total_query = "SELECT COUNT(*) FROM tabla_fronteras"

        query = f"""
            SELECT * FROM tabla_fronteras ORDER BY id_frontera ASC
            LIMIT {page_size} OFFSET {offset}
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(total_query)
                total = cursor.fetchone()[0]

                cursor.execute(query)
                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                respuesta = {
                    "total": total,
                    "objeto_pais_espanol": objeto_pais_espanol
                }

                return respuesta
    
    def buscar_union_pais_fronteras(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        # Consulta para obtener el número total de registros
        total_query = "SELECT COUNT(*) FROM union_pais_fronteras"
        
        query = f"""
            SELECT p.nombre_paises, f.nombre_frontera
            FROM union_pais_fronteras AS u
            JOIN tabla_pais_espanol AS p ON u.fk_pais = p.id_paises
            JOIN tabla_fronteras AS f ON u.fk_frontera = f.id_frontera
            ORDER BY p.nombre_paises
            LIMIT {page_size} OFFSET {offset}
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(total_query)
                total = cursor.fetchone()[0]

                cursor.execute(query)
                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pais_espanol)
                respuesta = {
                    "total": total,
                    "objeto_pais_espanol": objeto_pais_espanol
                }

                return respuesta

    def buscar_pais_fronteras(self):

        # Consulta para obtener el número total de registros
        query = f"""
            SELECT id_frontera, nombre_frontera FROM tabla_fronteras ORDER BY id_frontera ASC
        """

        query2 = f"""
            SELECT id_paises, nombre_paises FROM tabla_pais_espanol ORDER BY id_paises ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                fronteras = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_frontera_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in fronteras
                ]

                cursor.execute(query2)
                paises = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in paises
                ]
                
                respuesta = {
                    "objeto_frontera_espanol": objeto_frontera_espanol,
                    "objeto_pais_espanol": objeto_pais_espanol
                }

                return respuesta

    def agregar_pais_espanol(self, entrada: dict):
        query = f"""
            INSERT INTO public.tabla_pais_espanol
            (id_paises, nombre_paises, capital, area_km, continente, poblacion)
            VALUES ({entrada.get('id_paises')}, '{entrada.get('nombre_paises')}', '{entrada.get('capital')}', {entrada.get('area_km')}, '{entrada.get('continente')}', {entrada.get('poblacion')});
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def agregar_pais_traducciones(self, entrada: dict):
        query = f"""
            INSERT INTO public.tabla_nombre_pais_traducciones
            (id_traduccion, nombre_idioma, traduccion_oficial, traduccion_comun, fk_pais)
            VALUES ({entrada.get('id_traduccion')}, '{entrada.get('nombre_idioma')}', '{entrada.get('traduccion_oficial')}', '{entrada.get('traduccion_comun')}', '{entrada.get('fk_pais')}');
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def agregar_fronteras(self, entrada: dict):
        query = f"""
            INSERT INTO public.tabla_fronteras
            (id_frontera, nombre_frontera, longitud_frontera, descripcion_frontera, tipo_frontera)
            VALUES ({entrada.get('id_frontera')}, '{entrada.get('nombre_frontera')}', '{entrada.get('longitud_frontera')}', '{entrada.get('descripcion_frontera')}', '{entrada.get('tipo_frontera')}');
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def insertar_frontera_pais(self,  nombre_paises: str, nombre_frontera: str):
        #Consulta tabla_pais_espanol por nombre para traer id_paises
        query = f"""
            SELECT id_paises
            FROM tabla_pais_espanol
            WHERE nombre_paises = '{nombre_paises}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_paises = objeto_pais_espanol[0].get("id_paises")
        #Consulta tabla_fronteras por nombre para traer id_frontera
        query = f"""
            SELECT id_frontera
            FROM tabla_fronteras
            WHERE nombre_frontera = '{nombre_frontera}'
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
                response = cursor.fetchall()
                columnas = [columna.name for columna in cursor.description or []]
                objeto_pais_espanol = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                id_frontera = objeto_pais_espanol[0].get("id_frontera")
        #Consulta union_pais_fronteras el id_paises y id_frontera
        query = f"""
            INSERT INTO public.union_pais_fronteras
            (fk_pais, fk_frontera)
            VALUES ({id_paises}, {id_frontera});
            """
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)


    def actualizar_pais_espanol(self, entrada:dict):
        
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_pais_espanol
                SET {datos} = '{entrada[datos]}'
                WHERE id_paises = {entrada.get('id_paises')};
            """

            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.mogrify(query).decode())
                    cursor.execute(query)

    def actualizar_pais_traducciones(self, entrada:dict):
        
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_nombre_pais_traducciones
                SET {datos} = '{entrada[datos]}'
                WHERE id_traduccion = {entrada.get('id_traduccion')};
            """

            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.mogrify(query).decode())
                    cursor.execute(query)

    def actualizar_tabla_fronteras(self, entrada:dict):
        
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_fronteras
                SET {datos} = '{entrada[datos]}'
                WHERE id_frontera = {entrada.get('id_frontera')};
            """

            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.mogrify(query).decode())
                    cursor.execute(query)




