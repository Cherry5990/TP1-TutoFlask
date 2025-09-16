from .app import app
from flask import render_template, request

@app.route('/')
@app.route('/index/') # toujours mettre "/index/" au lieu de "/index" car sinon si on tape "/index/" on n'y accède pas
def index():
    # si pas de paramètres
    if len(request.args)==0:
        return render_template("index.html", title="R3.01 Dev Web avec Flask", name="Erika")
    else :
        param_name = request.args.get('name')
        return render_template("index.html", title="R3.01 Dev Web avec Flask", name = param_name)

@app.route('/about/')
def about():
    return render_template("about.html", title ="R3.01 Dev Web avec Flask - about")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title ="R3.01 Dev Web avec Flask - contact")

if __name__== "__main__":
    app.run()