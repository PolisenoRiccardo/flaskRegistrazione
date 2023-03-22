from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("login.html", methods = ['POST']) 

@app.route('/logged')
def logged():
    return render_template("logged.html") 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)