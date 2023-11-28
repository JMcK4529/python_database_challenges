# BookStore Model and Repository Classes Design Recipe

## 1. Design and create the Table

```
Table: books

Columns:
id | title | author_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
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
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

```python
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class StudentRepository

```

## 4. Implement the Model class

```python
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.author_name = ""

# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> book = Book()
# >>> book.title = "Dracula"
# >>> book.author_name = "Bram Stoker"
# >>> book.title
# 'Dracula'
# >>> book.author_name
# 'Bram Stoker'

    def __repr__(self):
        # => "Book(id, title, author_name)"

    def __eq__(self, other):
        # => True if self.id == other.id and self.title == other.title and 
        #                       self.author_name == other.author_name, else False

```

## 5. Define the Repository Class interface

```python
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, name, cohort_name FROM books;

        # Returns an array of Student objects.

```

## 6. Write Test Examples

These examples will later be encoded as Pytest tests.

```python
# 1
# Get all books

repo = BookRepository()

books = repo.all()

len(books) # =>  5

books[0].id # =>  1
books[0].title # =>  'Nineteen Eighty-Four'
books[0].author_name # =>  'George Orwell'

books[1].id # =>  2
books[1].title # =>  'Mrs Dalloway'
books[1].author_name # =>  'Virginia Woolf'
```

## 7. Test-drive and implement the Repository class behaviour