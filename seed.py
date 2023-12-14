from models import User, Song, Playlist, PlaylistSong, session
from datetime import datetime

# Clear existing data
session.query(User).delete()
session.query(Song).delete()
session.query(Playlist).delete()
session.query(PlaylistSong).delete()
session.commit()

# Seed User data
user_data = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "contact": "(555) 555-5555"},
    {"id": 2, "first_name": "Sarah", "last_name": "Jones", "email": "sarah.jones@gmail.com", "contact": "(404) 555-1234"},
    {"id": 3, "first_name": "Michael", "last_name": "Lee", "email": "michael.lee@hotmail.com", "contact": "(617) 555-9876"},
    {"id": 4, "first_name": "Amanda", "last_name": "Garcia", "email": "amanda.garcia@outlook.com", "contact": "(312) 555-3456"},
    {"id": 5, "first_name": "David", "last_name": "Miller", "email": "david.miller@yahoo.com", "contact": "(215) 555-7890"},
    {"id": 6, "first_name": "Jennifer", "last_name": "Brown", "email": "jennifer.brown@icloud.com", "contact": "(703) 555-2345"},
    {"id": 7, "first_name": "Matthew", "last_name": "Davis", "email": "matthew.davis@aol.com", "contact": "(818) 555-6789"},
    {"id": 8, "first_name": "Ashley", "last_name": "Williams", "email": "ashley.williams@verizon.net", "contact": "(901) 555-0123"},
    {"id": 9, "first_name": "James", "last_name": "Wilson", "email": "james.wilson@att.net", "contact": "(504) 555-4567"},
    {"id": 10, "first_name": "Jessica", "last_name": "Moore", "email": "jessica.moore@comcast.net", "contact": "(303) 555-8901"},
    {"id": 11, "first_name": "Daniel", "last_name": "Taylor", "email": "daniel.taylor@gmail.com", "contact": "(602) 555-2468"},
    {"id": 12, "first_name": "Emily", "last_name": "Martin", "email": "emily.martin@yahoo.com", "contact": "(415) 555-5678"},
    {"id": 13, "first_name": "William", "last_name": "Thomas", "email": "william.thomas@hotmail.com", "contact": "(713) 555-9012"},
    {"id": 14, "first_name": "Elizabeth", "last_name": "Lopez", "email": "elizabeth.lopez@outlook.com", "contact": "(310) 555-3579"},
    {"id": 15, "first_name": "Joshua", "last_name": "Clark", "email": "joshua.clark@icloud.com", "contact": "(805) 555-7901"},
    {"id": 16, "first_name": "Megan", "last_name": "Rodriguez", "email": "megan.rodriguez@aol.com", "contact": "(916) 555-1357"}
    # ... (continue the list)
]

users = [User(**datum) for datum in user_data]
session.add_all(users)
session.commit()

# Seed Song data
song_data = [
  {"id": 1, "name": "Song1", "category": "Rock", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 2, "name": "Summer Breeze", "category": "Pop", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 3, "name": "Rhythm of the Night", "category": "Electronic", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 4, "name": "Heartbeat", "category": "Hip Hop", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 5, "name": "Lost in the Clouds", "category": "Pop", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 6, "name": "Rebel Yell", "category": "Rock", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 7, "name": "Galactic Groove", "category": "Electronic", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 8, "name": "City Lights", "category": "Hip Hop", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 9, "name": "Whispers in the Wind", "category": "Pop", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()},
  {"id": 10, "name": "Highway to Nowhere", "category": "Rock", "Date_created": datetime.strptime("4/5/2023", "%m/%d/%Y").date()}
]

Song = [Song(**datum) for datum in song_data]
session.add_all(Song)
session.commit()

# Seed Playlist data
playlist_data = [
    {"id": 1, "user_id": 4, "created_at": datetime.now(), "total_songs": 5},
    {"id": 2, "user_id": 2, "created_at": datetime.now(), "total_songs": 9},
    {"id": 3, "user_id": 1, "created_at": datetime.now(), "total_songs": 11},
    {"id": 4, "user_id": 7, "created_at": datetime.now(), "total_songs": 21},
    {"id": 5, "user_id": 3, "created_at": datetime.now(), "total_songs": 27},
    {"id": 6, "user_id": 5, "created_at": datetime.now(), "total_songs": 22},
    {"id": 7, "user_id": 2, "created_at": datetime.now(), "total_songs": 2},
    {"id": 8, "user_id": 1, "created_at": datetime.now(), "total_songs": 6},
    {"id": 9, "user_id": 4, "created_at": datetime.now(), "total_songs": 12},
    {"id": 10, "user_id": 9, "created_at": datetime.now(), "total_songs": 7},

    # ... (continue the list)
]

playlists = [Playlist(**datum) for datum in playlist_data]
session.add_all(playlists)
session.commit()

# Seed PlaylistSong data
PlaylistSong_data = [
    {"id": 1, "playlist_id": 1, "song_id": 1},
    {"id": 2, "playlist_id": 2, "song_id": 2},
    # ... (continue the list)
]

PlaylistSong = [PlaylistSong(**datum) for datum in PlaylistSong_data]
session.add_all(PlaylistSong)
session.commit()

print("Done seeding data")
