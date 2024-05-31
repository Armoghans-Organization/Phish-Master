from flask import Flask , render_template, session, redirect, request
import sqlite3
from config import Config, db , cwd
import os
from utilities import banner

# Initialize the Flask app
app = Flask(__name__)

app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
        # Perform user authentication
        username = request.form['username']
        password = request.form['password']

        # Connect to the SQLite database
        conn = sqlite3.connect(os.path.join(cwd, 'PhishMaster.sqlite3'))
        cursor = conn.cursor()

        # Execute a query to check the username and password
        query = "SELECT * FROM user WHERE userName = ? AND password = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            # If authentication is successful, store user data in the session
            session['username'] = user[0]  # Assuming the username is in the first column
            session['logged_in'] = True
            conn.close()
            return redirect('/dashboard')

        # Authentication failed, show error message
        error_message = 'Invalid username or password'
        conn.close()
        return render_template('login.html', error_message=error_message)
  return render_template("index.html")

if __name__ == '__main__':
  #  Print Terminal Banner
  banner.print_banner()
  app.run(port=5000,debug=True)