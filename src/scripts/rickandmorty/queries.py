""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_tabla_personajes(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        query = f"""
            SELECT * FROM tabla_personajes ORDER BY id_personaje ASC
            LIMIT {page_size} OFFSET {offset} 
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
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

                return objeto_pais_espanol

    def buscar_tabla_especies(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        query = f"""
            SELECT * FROM tabla_especies ORDER BY id_especie ASC
            LIMIT {page_size} OFFSET {offset} 
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
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

                return objeto_pais_espanol

    def buscar_union_pais_personaje(self, page:int, page_size: int):

        offset = (page - 1) * page_size # filas que no se tienen en cuenta para mostrar

        query = f"""
            SELECT p.nombre_paises, pj.nombre_personaje
            FROM union_pais_personaje AS u
            JOIN tabla_pais_espanol AS p ON u.fk_pais = p.id_paises
            JOIN tabla_personajes AS pj ON u.fk_personaje = pj.id_personaje
            ORDER BY pj.nombre_personaje ASC
            LIMIT {page_size} OFFSET {offset} 
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
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

                return objeto_pais_espanol


    def agregar_personajes(self, entrada: dict):
        query = f"""
            INSERT INTO public.tabla_personajes
            (id_personaje, nombre_personaje, genero, origen, fk_especie)
            VALUES ({entrada.get('id_personaje')}, '{entrada.get('nombre_personaje')}', '{entrada.get('genero')}', '{entrada.get('origen')}', '{entrada.get('fk_especie')}');
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def agregar_especies(self, entrada: dict):
        query = f"""
            INSERT INTO public.tabla_especies
            (id_especie, nombre_especie, descripcion_especie, fecha_registro, alimentacion)
            VALUES ({entrada.get('id_especie')}, '{entrada.get('nombre_especie')}', '{entrada.get('descripcion_especie')}', '{entrada.get('fecha_registro')}', '{entrada.get('alimentacion')}');
        """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def insertar_personaje_pais(self, nombre_paises: str, nombre_personaje: str):
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
        #Consulta tabla_personajes por nombre para traer id_personaje
        query = f"""
            SELECT id_personaje
            FROM tabla_personajes
            WHERE nombre_personaje = '{nombre_personaje}'
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
                id_personaje = objeto_pais_espanol[0].get("id_personaje")
        #Consulta union_pais_personaje el id_paises y id_personaje
        query = f"""
            INSERT INTO public.union_pais_personaje
            (fk_pais, fk_personaje)
            VALUES ({id_paises}, {id_personaje});
            """
        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)


    def actualizar_tabla_personajes(self, entrada:dict):
        
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_personajes
                SET {datos} = '{entrada[datos]}'
                WHERE id_personaje = {entrada.get('id_personaje')};
            """

            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.mogrify(query).decode())
                    cursor.execute(query)

        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

    def actualizar_tabla_especies(self, entrada:dict):
        
        for datos in entrada:
            query = f"""
                UPDATE public.tabla_especies
                SET {datos} = '{entrada[datos]}'
                WHERE id_especie = {entrada.get('id_especie')};
            """

            with self._open_connection() as conn:
                with conn.cursor() as cursor:
                    print(cursor.mogrify(query).decode())
                    cursor.execute(query)

        
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)


