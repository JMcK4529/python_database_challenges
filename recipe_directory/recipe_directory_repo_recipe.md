# Student Model and Repository Classes Design Recipe

## 1. Design and create the Table

```
Table: recipes

Columns:
id | name | cooking_time | rating
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    cooking_time INT,
    rating INT
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO books (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
INSERT INTO books (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
INSERT INTO books (title, author_name) VALUES ('Emma', 'Jane Austen');
INSERT INTO books (title, author_name) VALUES ('Dracula', 'Bram Stoker');
INSERT INTO books (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 recipe_directory < seeds/recipe_directory.sql
```

## 3. Define the class names

```python
# Table name: recipes

# Model class
# (in lib/recipe.py)
class Recipe


# Repository class
# (in lib/Recipe_repository.py)
class RecipeRepository

```

## 4. Implement the Model class

```python
# Table name: recipes

# Model class
# (in lib/recipe.py)

class Book:
    def __init__(self, id, name, cooking_time, rating):
        self.id = 0
        self.name = ""
        self.cooking_time = 0
        self.rating = 0

    def __repr__(self):
        # => "Recipe(id, name, cooking_time, rating)"

    def __eq__(self, other):
        # => True if self.__dict__ == other.__dict__ else False
```

## 5. Define the Repository Class interface

```python
# Table name: recipes

# Repository class
# (in lib/recipe_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT * FROM recipes;

        # Returns an array of Recipe objects.

```

## 6. Write Test Examples

These examples will later be encoded as Pytest tests.

```python
# 1
# Get all recipes

repo = RecipeRepository()

recipes = repo.all()

len(recipes) # =>  5

books[0].id # =>  1
books[0].name # =>  'Hunter''s Chicken'
books[0].cooking_time # =>  40
recipes[0].rating # => 4

# 2
# Get the recipe with id == 1

repo = RecipeRepository()
recipes = repo.find(1) # => Recipe(1, Hunter's Chicken, 40, 4)
```

## 7. Test-drive and implement the Repository class behaviour