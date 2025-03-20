from flask import Flask, render_template, request, redirect, url_for
from models import db, Tarea

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def crear_tablas():
    db.create_all()

@app.route('/')
def index():
    tareas = Tarea.query.all()
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['POST'])
def agregar():
    descripcion = request.form['descripcion']
    nueva_tarea = Tarea(descripcion=descripcion)
    db.session.add(nueva_tarea)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = Tarea.query.get_or_404(id)
    if request.method == 'POST':
        tarea.descripcion = request.form['descripcion']
        tarea.completada = 'completada' in request.form
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('editar_tarea.html', tarea=tarea)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    tarea = Tarea.query.get_or_404(id)
    db.session.delete(tarea)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
