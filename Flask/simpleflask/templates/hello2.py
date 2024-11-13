from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def india():
    return "Hello, KLU"

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/emp/<int:emp1>')
def show_emp(emp1):
   return 'EMP ID Number %d' %emp1

@app.route('/sal/<float:sal1>')
def salary(sal1):
   return 'Salary Number %f' %sal1

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/login')
def login():
   return render_template("login.html")

if __name__ == "__main__":
    app.run()