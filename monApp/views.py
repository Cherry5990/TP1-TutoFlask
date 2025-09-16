from .app import app
from flask import render_template

@app.route('/')
@app.route('/index/') # toujours mettre "/index/" au lieu de "/index" car sinon si on tape "/index/" on n'y accède pas
def index():
    return render_template("index.html", title ="R3.01 Dev Web avec Flask", name="WTH ??!!")

@app.route('/about/')
def about():
    return render_template("about.html", title ="R3.01 Dev Web avec Flask - about")

@app.route('/contact/')
def contact():
    return render_template("contact.html", title ="R3.01 Dev Web avec Flask - contact")

if __name__== "__main__":
    app.run()