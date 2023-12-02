from lib.post import Post
from lib.comment import Comment

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            """SELECT posts.id AS post_id, posts.title AS post_title,
            posts.post_content, comments.id AS comment_id, 
            comments.comment_content, 
            comments.author_name
            FROM posts JOIN comments 
            ON posts.id = comments.post_id
            WHERE posts.id = %s;""",
            [post_id]
            )

        comments = []
        for row in rows:
            comments.append(Comment(
                             row["comment_id"], row["comment_content"],
                             row["author_name"], row["post_id"]
                             ))
        post = Post(rows[0]["post_id"], rows[0]["post_title"], 
                        rows[0]["post_content"], comments)
        return post