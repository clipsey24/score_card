from flask import Flask, redirect, render_template, request, url_for

from database import get_database

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/register', methods = ["POST", "GET"])
def register():
  if request.method ==  "POST":
    #Collect inforamation from html form.
    username = request.form['username']
    password = request.form['password']

    #connect to database.
    db = get_database()
    
    #sql query to insert the new values to database.
    db.execute("insert into users(username, password)values(?,?)",[username, password])

    #Make changes permanent in table
    db.commit()
    
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