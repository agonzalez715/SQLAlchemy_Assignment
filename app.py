"""Blogly application."""

from flask import Flask, render_template, redirect, url_for #imports the FLask class from the flask module which is used to create the flask application instance 
from models import db, connect_db #imports the db instance and the connect_db function from our models.py file 
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtention 


app = Flask(__name__) #creates an instance of the Flask applicaton, the __name__ variable represents the name of the current Python module 
app.config['DEBUG_TB_ENABLED'] = True  # Enable the toolbar
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # Don't intercept redirects
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly' #Configures the SQLAlchemy database URI to connect to a PostgreSQL database named 'blogly'. This URI format specifies the database type (postgresql), database name (blogly), and other optional parameters like host, port, username, and password if needed.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Disables SQLAlchemy's modification tracking feature, which can improve performance.
app.config['SQLALCHEMY_ECHO'] = True #Enables SQLAlchemy to echo SQL statements to the terminal, which can be helpful for debugging.

@app.route('/')
def index():
    return 'Hello, World!'

connect_db(app) #calls the connect_db function from the models.py file, passing the flask app instance as an argument this function typically configures the database connection and binds the SQLAlchemy instance to the Flask application
db.create_all() #Creates all database tables defined in your SQLAlchemy models. This command initializes the database structure based on your model definitions.

if __name__ == '__main__':
    app.run(debug=True)
