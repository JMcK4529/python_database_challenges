# Blog Directory - Two Tables Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.
```

```
Nouns:

post, title, content, comment, comment_content, author_name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| post                  | title, post_content
| comment               | comment_content, author_name

1. Name of the first table (always plural): `posts` 

    Column names: `title`, `post_content`

2. Name of the second table (always plural): `comments` 

    Column names: `comment_content`, `author_name`

## 3. Decide the column types

```
Table: posts
id: SERIAL
title: text
post_content: text

Table: comments
id: SERIAL
comment_content: text
author_name: text
```

## 4. Decide on The Tables Relationship

1. Can one post have many comments? Yes
2. Can one comment have many posts? No

1. **[POST] has many [COMMENTS]**
2. And on the other side, **[COMMENT] belongs to [POST]**
3. In that case, the foreign key is in the table [COMMENT]

## 5. Write the SQL

```sql
-- file: blog_directory.sql
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
  author_name int,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 blog < seeds/blog.sql
```
