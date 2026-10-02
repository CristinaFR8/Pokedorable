from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    proyecto = "Pokemon Battle Web"
    nombre = "Cristina Fernández"
    anio = 2026

    return render_template(
        'index.html',
        proyecto=proyecto,
        nombre=nombre,
        anio=anio
    )


if __name__ == '__main__':
    app.run('127.0.0.1', 5038, debug=True)