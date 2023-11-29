from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe_directory.sql")

# Retrieve all students
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
print("RecipeRepository#all():")
for recipe in recipes:
    print(f"    {recipe}")

# Retrieve and print student with id = 1
recipe1 = recipe_repository.find(1)
print(f"\nRecipeRepository#find(1):\n    {recipe1}")