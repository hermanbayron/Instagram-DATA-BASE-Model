import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    first_Name = Column(String(250), nullable=False)
    last_Name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    username = Column(Integer, nullable=False)
    birth_Name = Column(DateTime, nullable=False)
    post = relationship('Post', backref='usuarios', lazy='true')
    historias = relationship('Historia', backref='usuarios', lazy='true')
    post_guardado = relationship('Post_guardado', backref='usuarios', lazy='true')

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    fecha = Column(String(250), nullable=False)
    hora = Column(String(250), nullable=False)
    contenido = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    etiquetas = Column(String(250), nullable=False)
    hashtag = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    post_guardado = relationship('Post_guardado', backref='post', lazy='true')

class Historia(Base):
    __tablename__ = 'historias'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(250), nullable=False)
    fecha = Column(String(250), nullable=False)
    hora = Column(String(250), nullable=False)
    contenido = Column(String(250), nullable=False)
    multimedia = Column(String(250), nullable=False)
    etiquetas = Column(String(250), nullable=False)
    hashtag = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    post_guardado = relationship('Post_guardado', backref='historias', lazy='true')

    # Cambio de tablas

    # Post Guardado

Post_guardado = Table("post_guardado", Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("post", Integer, ForeignKey("post.id")),
    Column("usuarios", Integer, ForeignKey("usuarios.id")),
    Column("historias", Integer, ForeignKey("historias.id"))
    )

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')