from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():

    res_text = ""
    res2_text = ""

    if request.method == 'POST':
        print("Dados do formulário:", request.form)
        cep = request.form.get('cep')

        if cep:
            print("CEP recebido:", cep)
            res = req.post('http://127.0.0.1:8000', json={'cep': cep})
            res_text = res.text
            print("Resposta do POST:", res_text)
        else:
            print("Nenhum CEP recebido.")

    res2 = req.get('http://127.0.0.1:8000/cep')
    res2_text = res2.text
    print("Resposta do GET:", res2_text)

    return render_template('index.html', res=res_text, res2=res2_text)

if __name__ == '__main__':
    app.run(debug=True, port=7000)
