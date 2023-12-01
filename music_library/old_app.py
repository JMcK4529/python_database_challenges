from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
print("ArtistRepository#all():")
for artist in artists:
    print(f"    {artist}")

# Retrieve all albums
album_repository = AlbumRepository(connection)
albums = album_repository.all()

# List albums to terminal
print("\nAlbumRepository#all():")
for album in albums:
    print(f"    {album}")

# Retrieve album with id = 1
album1 = album_repository.find(1)
print(f"\nAlbumRepository#find(1): {album1}")