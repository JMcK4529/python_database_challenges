from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts;")
        posts = []
        for row in rows:
            post = Post(row["id"], row["title"], row["content"], 
                         row["views"], row["user_account_id"])
            posts.append(post)
        return posts

    def find(self, post_id):
        row = self._connection.execute(
            "SELECT * FROM posts WHERE id = %s;",
              [post_id]
              )[0]
        return Post(row["id"], row["title"], row["content"], 
                         row["views"], row["user_account_id"])

    def create(self, post):
        self._connection.execute(
            "INSERT INTO posts (title, content, views, user_account_id)" +
            " VALUES (%s, %s, %s, %s);", 
            [post.title, post.content, post.views, post.user_account_id]
            )
        return None

    def delete(self, post_id):
        self._connection.execute(
            "DELETE FROM posts WHERE id = %s;",
            [post_id]
        )
        return None