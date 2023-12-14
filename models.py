from sqlalchemy import Column, Integer, Date, VARCHAR, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Create tables
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR)
    last_name = Column(VARCHAR)
    email = Column(VARCHAR)
    contact = Column(Integer)
    playlists = relationship('Playlist', back_populates='user')

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR)
    artist = Column(VARCHAR)
    duration = Column(Integer)
    category = Column(VARCHAR)
    Date_created = Column(Date)
    playlists = relationship('PlaylistSong', back_populates='song')

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='playlists')
    created_at = Column(Date)
    total_songs = Column(Integer)
    songs = relationship('PlaylistSong', back_populates='playlist')

class PlaylistSong(Base):
    __tablename__ = 'playlist_songs'
    id = Column(Integer, primary_key=True)
    playlist_id = Column(Integer, ForeignKey('playlists.id'))
    playlist = relationship('Playlist', back_populates='songs')
    song_id = Column(Integer, ForeignKey('songs.id'))
    song = relationship('Song', back_populates='playlists')

engine = create_engine('sqlite:///site.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
