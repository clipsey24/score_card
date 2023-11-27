from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/logout')
def logout():
  return render_template('home.html')

@app.route('/layout')
def layout():
  return render_template('layout.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)