# Escrutinio

Herramienta hecha en Python para ayudar al escrutinio de cualquier votación.

## Ficheros de datos

En la carpeta `data` es donde deben residir los ficheros "crudos" del volcado de la votación.

### `<fichero>.dat`

- Cada línea que comience con `#` es ignorada y permite incorporar comentarios.
- Cada línea contiene la información de una papeleta. Los posibles valores son:
    - Números separados por espacios. Cada número identifica una elección (ordenadas en el fichero `<fichero>.key`)
    - `B` indicando que es un **voto en blanco**.
    - `N` indicando que es un **voto nulo**.

### `<fichero>.key`

- Cada línea que comience con `#` es ignorada y permite incorporar comentarios.
- Las líneas sin comentarios serán tratadas como las posibles elecciones de la votación. Según su orden en el fichero, se identificarán con los códigos 1, 2, 3, ... (así aparecerán en el fichero `<fichero>.dat`)

## Lanzar la herramienta

~~~console
$> pipenv install   # instalar dependencias
$> pipenv run python counting.py data/ce1819.dat  # ejemplo de fichero
~~~
