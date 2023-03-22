from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home(): 
  return render_template("index.html", methods = ['POST']) 

@app.route('/logged', methods = ['POST'])
def logged():
    Password = request.form['password']
    Conferma = request.form['conferma']
    if Conferma == Password:
      Email = request.form['mail']
      if '@' in Email:
        Nome = request.form['nome']
        Cognome = request.form['cognome']
        Data = request.form['data']
        Nazioni = request.form['nazione']
        Username = request.form['username']
        Lingue = request.form.getlist('lingue')
        Consenso = request.form.getlist('consenso')
        return render_template("logged.html", Nome = Nome, Cognome = Cognome, Data = Data, Nazioni = Nazioni, Username = Username, Email = Email, Lingue = Lingue, Consenso = Consenso, Password = Password) 
      else:
        return render_template("errore1.html") 
    else:
      return render_template("errore.html") 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)