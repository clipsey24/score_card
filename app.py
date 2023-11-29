from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods = ["POST", "GET"])
def register():
  if request.method ==  "POST":
    username = request.form['username']
    password = request.form['password']
  #sql query to insert thewe to database.
  return redirect(url_for("login"))  
  return render_template('register.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/logout')
def logout():
  return render_template('home.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)