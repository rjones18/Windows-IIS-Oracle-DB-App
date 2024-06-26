from flask import Flask, request, render_template, redirect, url_for
from models import Employee, db_session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        new_employee = Employee(name=name, age=age)
        db_session.add(new_employee)
        db_session.commit()
        return redirect(url_for('employees'))
    employees = db_session.query(Employee).all()
    return render_template('employees.html', employees=employees)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=True) 
