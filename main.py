import os

from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)
app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_USER']     = os.environ.get("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD")
app.config['MYSQL_DB'] 		 = os.environ.get("MYSQL_DB")
app.config['MYSQL_HOST'] 	 = os.environ.get("MYSQL_HOST")
mysql.init_app(app)

@app.route("/")
def main():
	cursor = mysql.connect.cursor()
	cursor.execute("SELECT version();")
	data = cursor.fetchone()
	return "Welcome! " + str(data)

if __name__ == "__main__":
    app.run()