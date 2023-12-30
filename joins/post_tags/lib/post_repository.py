from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            """
            SELECT * FROM posts;
            """
        )
        posts = []
        for row in rows:
            posts.append(Post(row['id'], row['title']))
        return posts

    def find_by_id(self, id):
        row = self._connection.execute(
            """
            SELECT * FROM posts WHERE id=%s;
            """, [id]
        )[0]
        return Post(row['id'], row['title'])

    def find_by_tag(self, tag):
        rows = self._connection.execute(
            """
            SELECT posts.id as post_id, posts.title as post_title,
            tags.id as tag_id, tags.name as tag_name
            FROM posts
            JOIN posts_tags ON posts.id = posts_tags.post_id 
            JOIN tags ON posts_tags.tag_id = tags.id
            WHERE tags.name = %s;
            """, [tag]
        )
        posts = []
        for row in rows:
            posts.append(Post(row['post_id'], row['post_title']))
        return posts