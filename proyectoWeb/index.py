#Importar Framework Flask
from flask import   Flask, render_template
app = Flask (__name__)
#En caso de que no aparezca la pag
@app.before_request
def before_request():
    print ("Antes de la petición...")

@app.after_request
def after_request(response):
    print ("Después de la petición...")
    return response
#Crear las rutas hacia las paginas html
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
@app.route('/CaraACara')
def CaraACara():
    return render_template('CaraACara.html')
@app.route('/Chat')
def Chat():
    return render_template('Chat.html')
@app.route('/WP')
def WP():
    return render_template('WP.html')
@app.route('/registro')
def Registro():
    return render_template('Registro.html')
@app.route('/habilidades')
def habilidades():
    return render_template('habilidades.html')
#3 - Definir que corra la app
if __name__=='__main__':
    app.run(debug=True)


