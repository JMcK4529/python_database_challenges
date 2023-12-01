from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
  def __init__(self):
    self._connection = DatabaseConnection()
    self._connection.connect()
    self._connection.seed("seeds/music_library.sql")

  def run(self):
    # "Runs" the terminal application.
    # It might:
    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
    #   * Query the database
    #   * Display some output
    # We're going to print out the artists!
    artist_repo = ArtistRepository(self._connection)
    album_repo = AlbumRepository(self._connection)
    print("Welcome to the music library manager!")
    print("What would you like to do?")
    input_valid = False
    while not input_valid:
        user_input = input(
        "    1. List all albums\n    2. List all artists\n").strip()
        try:
           user_input = int(user_input)
           if user_input in [1, 2]:
              input_valid = True
        except Exception:
           pass
    if user_input == 1:
       albums = album_repo.all()
       for album in albums:
          print(album)
    elif user_input == 2:
       artists = artist_repo.all()
       for artist in artists:
          print(artist)

if __name__ == '__main__':
    app = Application()
    app.run()