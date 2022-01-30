from distutils.log import debug
from flask import Flask,render_template
from pkg_resources import Requirement

app = Flask(__name__) # padrão flask


@app.route('/') #caminho depois do meu domínio, a barrinha só significa primeira página


def homepage():# função significa oque você quer exibir naquela pagina
    return render_template('pagina1.html')# é preciso retornar um valor da função para a página 'pagina1.html' chama o html 

if __name__=='__main__':#esse if é p não da problema no servidor

    app .run(debug=True)# debug=True é pro sit atualizar sozinho 
