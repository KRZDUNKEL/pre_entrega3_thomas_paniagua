# pre_entrega3_thomas_paniagua
# Mi Proyecto Django - MVT Pattern

Este proyecto sigue el patrón MVT de Django y tiene las siguientes características:

1. **Herencia de HTML**:
    - La plantilla base se encuentra en `templates/base.html`.

2. **Modelos**:
    - Se han creado tres modelos en `myapp/models.py`: Category, Product, y Customer.

3. **Formularios**:
    - Hay formularios para insertar datos en cada una de las clases del modelo en `myapp/forms.py`.

4. **Búsqueda en la BD**:
    - Existe un formulario de búsqueda en `myapp/forms.py` y una vista asociada en `myapp/views.py`.

5. **Orden para probar funcionalidades**:
    - 1. Crear una nueva categoría: `/create/category/`
    - 2. Crear nuevos productos y clientes (rutas respectivas).
    - 3. Realizar búsquedas en la base de datos: `/search/`

Para probar las funcionalidades, accede a cada ruta mencionada y sigue las instrucciones en la página.
