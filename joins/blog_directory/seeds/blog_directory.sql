-- file: blog_directory.sql

DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS posts;

-- Create the table without the foreign key first.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  author_name text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

INSERT INTO posts (title, post_content) VALUES ('Title 1', 'Content 1');
INSERT INTO posts (title, post_content) VALUES ('Title 2', 'Content 2');

INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 1', 'Author 1', 1);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 2', 'Author 2', 1);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 3', 'Author 1', 2);
INSERT INTO comments (comment_content, author_name, post_id) VALUES ('Comment 4', 'Author 2', 2);