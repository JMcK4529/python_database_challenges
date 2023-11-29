from lib.recipe import Recipe

"""
Recipe construsts with an id, name, cooking_time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Title", 1000, 5)
    assert recipe.id == 1
    assert recipe.name == "Test Title"
    assert recipe.cooking_time == 1000
    assert recipe.rating == 5

"""
Recipes are formatted to strings in a readable way
"""
def test_recipe_to_string():
    recipe = Recipe(1, "Test Title", 1000, 5)
    assert str(recipe) == "Recipe(1, Test Title, 1000, 5)"

"""
Comparing two instances of Recipe with the same data should
result in them being equal
"""
def test_recipe_equality():
    recipe1 = Recipe(1, "Test Title", 1000, 5)
    recipe2 = Recipe(1, "Test Title", 1000, 5)
    assert recipe1 == recipe2