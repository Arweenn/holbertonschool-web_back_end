#!/usr/bin/env python3
""" User model """

# Importing necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating a base class for declarative models
Base = declarative_base()

# Defining the User class


class User(Base):
    """User class to interact with the ORM"""

    # Defining the table name
    __tablename__ = 'users'

    # Defining the columns of the table
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    hashed_password = Column(String(250))
    session_id = Column(String(250))
    reset_token = Column(String(250))

    # Specifying additional table arguments
    __table_args__ = {'extend_existing': True}

    # Initializing the User instance
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    # String representation of the User instance
    def __repr__(self):
        return "User: {}".format(self.email)
