from flask import Flask, render_template, request, redirect


app = Flask(__name__)
class cadinfluecer:
    def __init__(self, nome, plataforma, seguidores, areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas
lista = []

@app.route('/')
def hello_world():
    return 'começando!'


@app.route('/influ')
def influ():
    return render_template('influ.html', Titulo="Influenciers: ", Listainflu=lista)


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', Titulo= "Cadastro Influencers")

@app.route("/criar", methods= ['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    areas = request.form['areas']
    obj= cadinfluecer( nome, plataforma, seguidores, areas)
    lista.append(obj)
    return redirect('/influ')

if __name__ == '__main__':
    app.run()
