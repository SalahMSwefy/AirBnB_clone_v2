#!/usr/bin/python3
"""This module instantiates an object of class DBStorage
"""
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

class DBStorage:
    '''Database storage class'''
    __engine = None
    __session = None
    
    def __init__(self):
        '''Constructor'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        '''Query on the current database session'''
        new_dict = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        else:
            for c in classes:
                for obj in self.__session.query(c).all():
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        '''Add the object to the current database session'''
        self.__session.add(obj)
        
    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()
        
    def delete(self, obj=None):
        '''Delete from the current database session obj if not None'''
        if obj:
            self.__session.delete(obj)
            
    def reload(self):
        '''Create all tables in the database'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def close(self):
        '''Close the current session'''
        self.__session.close()
    
    