# !/usr/bin/env python3
import click
from models import User, Song, Playlist, PlaylistSong, session
from datetime import datetime
#from sqlalchemy.orm import session

@click.command()
def add_user():
    click.echo('Adding a new user...')
    first_name = click.prompt('Enter first_name', type=str)
    last_name = click.prompt('Enter last_name', type=str)
    email = click.prompt('Enter email', type=str)
    contact = click.prompt('Enter contact', type=str)
    
    click.echo(f'User {first_name} {last_name}, {email}, {contact} successfully added!')

    new_user = User(first_name=first_name, last_name=last_name, email=email, contact=contact)
    session.add(new_user)
    session.commit()

@click.command()
def add_song():
    click.echo('Adding a song...')
    title = click.prompt('Enter song title')
    artist = click.prompt('Enter artist')
    duration = click.prompt('Enter duration in seconds')
    category = click.prompt('Enter song category')
    Date_created = click.prompt('Enter date created')

    click.echo(f'{title}, {artist}, {duration}, {category}, {Date_created} sucessfully added!')

    new_song = Song(name=title, artist=artist, duration=duration)
    session.add(new_song)
    session.commit()

@click.command()
def add_playlist():
    click.echo("Adding a playlist...")
    user_id = click.prompt('Enter user ID')

    creation_date_input = click.prompt('Enter creation date (YYYY-MM-DD)')
    created_at = datetime.strptime(creation_date_input, "%Y-%m-%d").date()
    total_songs = click.prompt('Enter total songs')

    click.echo(f'User_id {user_id} successfully added playlist!')

    new_playlist = Playlist(user_id=user_id, created_at=created_at, total_songs=total_songs)
    session.add(new_playlist)
    session.commit()

@click.command()
def add_to_playlist():
    click.echo("Adding a song to playlist...")
    playlist_id = click.prompt('Enter playlist ID')
    song_id = click.prompt('Enter song ID')
    click.echo(f'The playlist {playlist_id} has added song {song_id} successfully')

    new_playlist_song = PlaylistSong(playlist_id=playlist_id, song_id=song_id)
    session.add(new_playlist_song)
    session.commit()

#if __name__ == '__main__':
exit_loop = False 
while not exit_loop:
    click.secho("*******************MUSIC PLAYLIST MANAGER*******************", fg='bright_cyan')
    click.secho("What would you like to do?", fg='bright_yellow')
    click.secho("................................................")
    click.secho("1. Add a new user", fg='bright_green')
    click.secho("2. Add a new song", fg='bright_green')
    click.secho("3. Add a new playlist for a user", fg='bright_green')
    click.secho("4. Add a song to a playlist", fg='bright_green')
    click.secho("5. Exit", fg='bright_green')
    
    option = click.prompt(">", type=int)
    if option == 1:
        add_user()
    elif option == 2:
        add_song()  
    elif option == 3:
        add_playlist()  
    elif option == 4:
        add_to_playlist() 
    elif option == 5:
        exit_loop = True
    else:
        click.echo("Invalid option", fg='bright_red')
