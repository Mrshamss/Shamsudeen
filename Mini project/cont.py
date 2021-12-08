from flask import Flask, render_template,request, redirect
from db import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM Login")
    Logins = mycursor.fetchall()
    return render_template('index.html', logins = Logins)


@app.route('/Gotologinn')
def login():
    return redirect('/Login')




@app.route('/add', methods=['GET', 'POST'])
def add_Login():
    if request.method == 'GET':
        return redirect('/Student')
    if request.method == 'POST':
          # _ = request.form['name']
        _User_name = request.form['User_name']
        _Email = request.form['Email']
        sql = 'INSERT INTO Login (Email,user_name) VALUE (%s, %s)'
        val = (_User_name, _Email)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/Student')





    
    
@app.route('/details/<int:id>')
def Login_details(id):
    mycursor.execute(f'SELECT * FROM Login WHERE ID={id}')
    Login = mycursor.fetchone()
    return render_template('Login_detail.html', Login = Login)





@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_Login(id):
    if request.method == 'GET':
        mycursor.execute(f'SELECT * FROM Login WHERE ID={id}')
        Login = mycursor.fetchone()
        return render_template('Login_edit.html', Login = Login)
    if request.method == 'POST':
        _User_name = request.form['User_name']
        _Password = request.form['Password']
        _Email = request.form['Email']
        sql = f'UPDATE login SET User_name = %s, Password = %s, Email = %s WHERE ID = %s',
        values = (_User_name, _Password, _Email, id)
        mycursor.execute(sql, values)
        mydb.commit()
        return redirect('/')
    
    

@app.route('/delete/<int:id>')
def delete_Login(id):
    sql = f'DELETE FROM Login WHERE ID={id}'
    mycursor.execute(sql)
    mydb.commit()
    return redirect('/')



@app.route('/Student')
def stundentstuff():
    return render_template('Student.html')


@app.route('/Login')
def loginpage():
    return render_template('Login_form.html')

@app.route('/Make_Payment')
def paymentpage():
    return render_template('Payment.html')


# @app.route('/back')
# def back():
#     mycursor.execute("SELECT * FROM Student")
#     Student = mycursor.fetchall()
#     return render_template('details.html', Student = Student)
# @app.route('/clear')
# def clear():
#     return render_template('Student.html')
# @app.route('/delete/>int:id')
# def delete_Student():
#     sql = f'DELETE FROM Student WHERE ID={id}'
#     mycursor.execute(sql)
#     mydb.commit()
#     return redirect('/')



@app.route('/addstudent', methods=['GET', 'POST'])
def add_Student():
    if request.method == 'POST':
        # return redirect('/Reciept')
        _First_Name = request.form['First_Name']
        _Last_Name = request.form['Last_Name']
        _Age = request.form['Age']
        _Deparment = request.form['Department']
        _Phone_No = request.form['Phone_No']
        _Email = request.form['Email']
        sql = 'INSERT INTO Student(First_Name, Last_Name, Age, Department, Phone_No, Email) VALUES ( %s, %s, %s, %s, %s, %s)'
        val = (_First_Name,  _Last_Name, _Age, _Deparment, _Phone_No, _Email)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/Make_Payment')
    
    
    
    

    
@app.route('/addpayment', methods=['GET', 'POST'])
def makepayment():
    if request.method == 'POST':
        _Student_Name = request.form['Student_Name']
        _Student_ID = request.form['Student_ID']
        _Amount = request.form['Amount']
        _Deparment = request.form['Department']
        _Phone_No = request.form['Phone_No']
        _Email = request.form['Email']
        _Date = request.form['Date']
        _Reciept_No = request.form['Reciept_No']
        
        
        sql = 'INSERT INTO Make_Payment(Student_Name, Student_ID, Amount, Department, Phone_No, Email, Data, Reciept_No) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (_Student_Name, _Student_ID, _Amount, _Deparment, _Phone_No, _Email, _Date, _Reciept_No)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')
    
        
    
    
# @app.route('/details/<int:id>')
# def student_details(id):
#     mycursor.execute(f'SELECT * FROM Student WHERE ID={id}')
#     Student = mycursor.fetchone()
#     return render_template('student_detail.html', Student = Student)




# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit_student(id):
#     if request.method == 'GET':
#         mycursor.execute(f'SELECT * FROM Student WHERE ID={id}')
#         Student = mycursor.fectchone()
#         return render_template('student_edit.html', Student = Student)
#     if request.method == 'POST':
#         _First_Name = request.form['First_Name']
#         _Last_Name = request.form['Last_Name']
#         _Age = request.form['Student_ID']
#         _Department = request.form['Department']
#         _Phone_No = request.form['Phone_No']
#         _Email = request.form['Email']
#         sql = f'UPDATE Student SET First_Name = %s, Last_Name = %s, Age = %s, Department = %s, Phone_No = %s, Email = %s WHERE ID = %s',
#         values = (_First_Name, _Last_Name, _Age, _Department, _Phone_No, _Email, id)
#         mycursor.execute(sql, values)
#         mydb.commit()
#         return redirect('/')
    
    

# @app.route('/delete/<int:id>')
# def delete_Student(id):
#     sql = f'DELETE FROM Student WHERE ID={id}'
#     mycursor.execute(sql)
#     mydb.commit()
#     return redirect('/')



    
    


if __name__ == '__main__':
        app.run(debug=True)




