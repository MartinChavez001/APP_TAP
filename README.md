# TP Final
Trabajo de Tecnicas Avanzadas de la Programacion

Integrantes:
    Miguel Centeno
    Julian Simbron
    Martin Chavez

Descripcion:
    Elaboramos una simple pagina en la cual podemos ver las cotizaciones de distintos tipos de activos, en este caso el dolar, en relacion al peso argentino.
    Con el fin de tener una pagina a mano para poder ver si estos suben o bajan su precio. La pagina esta desarrollada en Django para el backend, y utilizamos
    HTML, CSS y Bootstrap para el frontend.
    'APIS': Utilizamos la API dolarAPI, la cual nos devuelve el precio de los activos.
    'MVC': Models.py maneja las tablas y entidades de la base de datos. Templates, maneja el apartado visual donde estan el archivo Index.html, y Views.py maneja la logica del backend para servirla en el archivo HTML
    'Crud': CREATE: Crear favoritos. Read: Lectura del los datos recopilados por la BD. Delete: Quitar de favoritos los activos no deseados. UPDATE: Los datos de las cotizaciones se actualizan de forma automatica cuando hay un cambio.
    BD entreladazas: Cotizacion guarda el tipo de dolar, el precio y la fecha de actualizacion. Mientras que la tabla Favorito es la seleccion del usuario donde guarda de forma personal los activos que le interesa.
