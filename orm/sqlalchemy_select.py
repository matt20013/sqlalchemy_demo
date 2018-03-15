# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from sqlalchemy_declarative import Address, Base, Person
 
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

if (session.query(Person).count() > 0):

    print("Iterate..\n")
    # Insert a Person in the person table
    for instance in session.query(Person).order_by(Person.name):
        print(instance.name)
    
    
    print("Filter..\n")
    for instance in session.query(Person).filter(Person.name.like('M%')).order_by(Person.name):
        print(instance.name)
    
    print("Count..\n")
    print(session.query(Person).count())
    
    print("First..\n")
    person = session.query(Person).filter(Person.name.like('M%')).order_by(Person.name).first()
    print(person.name)
    
else:
    print("No records")