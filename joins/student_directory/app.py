from lib.database_connection import DatabaseConnection
from lib.cohort_repository import CohortRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/student_directory_2.sql")

class App:
    """Runs the find_with_students method to find
    the cohort with id = 1 and its students"""
    def __init__(self):
        repo = CohortRepository(connection)
        print(repo.find_with_students(1))

if __name__ == "__main__":
    app = App()