from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)
    posts = relationship("Post")
    comments = relationship("Comment")
    favorites = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    sw_entity_id = Column(Integer, ForeignKey('sw_entity.ID'))
    user = relationship("User")
    sw_entity = relationship("SWEntity")

class SWEntity(Base):
    __tablename__ = 'sw_entity'
    ID = Column(Integer, primary_key=True)
    name = Column(String(250))
    type = Column(Enum('planet', 'character', name='sw_entity_type'))

# Rest of your schema remains the same...

engine = create_engine('sqlite:///starwars_blog.db')
Base.metadata.create_all(engine)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
