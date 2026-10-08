# Pokémon Battle Web

Aplicación web desarrollada con **Python y Flask** para consultar información sobre diferentes Pokémon y visualizar sus características.

El proyecto forma parte del módulo **Desarrollo Web en Entorno Servidor (DWES)** y utiliza **Jinja2** para generar las páginas HTML a partir de los datos proporcionados en un fichero JSON.

**Autora:** Cristina Fernández
**Curso:** 2026/27

## Descripción

La aplicación permite consultar una selección de Pokémon a través de diferentes vistas:

* Página principal de bienvenida.
* Listado de Pokémon disponibles.
* Vista detallada de cada Pokémon.
* Información sobre sus tipos, características y otros datos.
* Clasificación del Pokémon según su peso.
* Representación gráfica de sus estadísticas.
* Listado de sus ataques.
* Navegación entre el listado y las páginas de detalle.

Los datos de los Pokémon se obtienen del fichero `data/pokemons-cute.json`, que se carga al iniciar la aplicación.

## Tecnologías utilizadas

* Python 3
* Flask
* Jinja2
* HTML5
* CSS3

## Estructura del proyecto

```text
Pokemon-Battle-Web/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── pokemons-cute.json
└── app/
    ├── main.py
    ├── static/
    │   ├── css/
    │   │   └── estilos.css
    │   └── img/
    │       └── pokemon-battle.png
    └── templates/
        ├── base.html
        ├── index.html
        ├── pokemons.html
        └── pokemon.html
```

> El entorno virtual `venv/` se crea localmente y no se incluye en el repositorio.

## Requisitos

Para ejecutar el proyecto es necesario tener instalado:

* Python 3
* Git

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/CristinaFR8/Pokemon-Battle-Web.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd Pokemon-Battle-Web
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows:

```bash
.\venv\Scripts\activate
```

Una vez activado, aparecerá `(venv)` al principio de la terminal.

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Las versiones de las dependencias utilizadas están especificadas en `requirements.txt` para facilitar la reproducción del entorno del proyecto.

## Ejecución

Con el entorno virtual activado:

```bash
python app/main.py
```

La aplicación estará disponible en:

```text
http://127.0.0.1:5038/
```

Abrir esta dirección en el navegador para acceder a la aplicación.

Si no se puede activar el entorno virtual, también se puede ejecutar directamente el Python incluido en `venv`:

```bash
.\venv\Scripts\python app/main.py
```

## Vistas de la aplicación

### Página principal

```text
/
```

Muestra la bienvenida a la aplicación y permite acceder al listado de Pokémon.

### Listado de Pokémon

```text
/pokemons/
```

Muestra los Pokémon disponibles y permite acceder a la información detallada de cada uno.

### Detalle de un Pokémon

```text
/pokemons/<id>/
```

Muestra información detallada del Pokémon seleccionado, incluyendo:

* Nombre e imágenes.
* Altura y peso.
* Tipo.
* Clasificación según el peso.
* Estadísticas representadas gráficamente.
* Ataques y sus características.
* Otros datos disponibles en el JSON.

## Datos

Los datos utilizados por la aplicación se encuentran en:

```text
data/pokemons-cute.json
```

El fichero se carga una única vez al iniciar el servidor y los datos quedan disponibles para las diferentes rutas de la aplicación.

## Plantillas

Las páginas HTML utilizan **Jinja2**.

Se utiliza una plantilla base:

```text
app/templates/base.html
```

sobre la que se construyen las diferentes vistas mediante herencia de plantillas.

Las rutas internas y los recursos estáticos se generan utilizando `url_for`.

## Autoría

**Cristina Fernández**
**DWES · 2026/27**
