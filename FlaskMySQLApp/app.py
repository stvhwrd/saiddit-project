from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv
import sys  # for stderr

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'csc370'
app.config['MYSQL_DATABASE_PASSWORD'] = 'project'
app.config['MYSQL_DATABASE_DB'] = 'saiddit'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showLogIn')
def showLogIn():
    return render_template('login.html')
<<<<<<< HEAD
    
@app.route('/logIn', methods=['POST','GET'])
def logIn():
    try:
        username = request.form['inputName']
        password = request.form['inputPassword']
        
        conn = mysql.connect()
        cursor = conn.cursor()
        
        # If we got the username and password
        if username and password:
            
            cursor.execute("SELECT password FROM Accounts WHERE username='"+username+"'")
            password_hash = str(cursor.fetchone())[3:83] # becuase mysql adds 'u' to the front of the string and ',) to the end. Because we're converting from a tuple?
            sys.stderr.write(password+"\n")
            sys.stderr.write(password_hash+"\n")
            # check if password is correct else say that it was incorrect password or username
            if check_password_hash(password_hash,password):
                sys.stderr.write("correct username and password")
                return json.dumps({'html':'<span>Enter the required fields</span>'})
            else:
               sys.stderr.write("Incorrect username or password")
               return json.dumps({'html':'<span>Enter the required fields</span>'})
    except Exception as e:
        sys.stderr.write(str(e))
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        conn.close()     
 
@app.route('/signUp', methods=['POST','GET'])
=======


@app.route('/signUp', methods=['POST', 'GET'])
>>>>>>> 7b6e3d9b08ffca3558edae95c7d225865d5cc680
def signUp():
    try:
        username = request.form['inputName']
        password = request.form['inputPassword']
<<<<<<< HEAD
       
=======
        hashed_password = generate_password_hash(password, method="sha256", salt_length=8)

>>>>>>> 7b6e3d9b08ffca3558edae95c7d225865d5cc680
        conn = mysql.connect()
        cursor = conn.cursor()

        # validate the received values
        if username and password:
<<<<<<< HEAD
            hashed_password = generate_password_hash(password,method="sha256", salt_length=8)
            insert_stmt =  "INSERT INTO Accounts (username,password) VALUES (%s, %s)"
=======
            insert_stmt = "INSERT INTO Accounts (username,password) VALUES (%s, %s)"
>>>>>>> 7b6e3d9b08ffca3558edae95c7d225865d5cc680
            data = (username, hashed_password)
            cursor.execute(insert_stmt, data)
            info = cursor.fetchone()

            if info is None:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        sys.stderr.write(str(e))
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    app.run(host=getenv('IP', '0.0.0.0'), port=int(getenv('PORT', 8080)))
