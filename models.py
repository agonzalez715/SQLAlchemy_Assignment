"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime #this is an optional import for time stamps 

db = SQLAlchemy() #this line creates the instance of the SQLAlchemy class and assigns it to a variable db,
                    #we will use this to interact with the database, define models. and perdoem dabase operations

class User(db.Model): #this line defines the 'user' class as a subclass of 'db.model' indicating that User is an SQLAlchemy model that maps to a database table
    __tablename__ = 'users'; #this  line specifies the name of the datanase tanle wqhere user data will be stored
                            #in this case, its users
#the few lines below are defining the db columns, their data type, and whether or not they can be null 
    id = db.Column(db.Integer, primary_key=True) #auto incrementing primary key that serves as the unique identifier
    first_name = db.Column(db.String(50), nullable=False) #column hplding first name data with string datatype
    last_name = db.Column(db.String(50), nullable=False) #column for last name and datatype 
    image_url = db.Column(db.String(200), default='default.jpg') #assuming a default image URL

    #optional timestamp, inside the users class so remember to indent 

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)