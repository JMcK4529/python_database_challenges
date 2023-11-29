from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
RecipeRepository.all returns all the recipes (and all columns) from
the database
"""
def test_all_records_retrieved_by_all_method(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)

    recipes = repository.all()

    assert recipes == [
        Recipe(1, "Hunter's Chicken", 40, 3),
        Recipe(2, "Spaghetti Carbonara", 25, 4),
        Recipe(3, "Sweet and Sour Pork Balls", 50, 2),
        Recipe(4, "Ham Sandwich", 5, 1),
        Recipe(5, "Nut Roast", 80, 5)
    ]

"""
RecipeRepository.find(n) returns the Recipe whose id == n
"""
def test_single_student_with_correct_id_retrieved_by_find(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    repository = RecipeRepository(db_connection)
    recipe = repository.find(3)
    assert recipe == Recipe(3, "Sweet and Sour Pork Balls", 50, 2)