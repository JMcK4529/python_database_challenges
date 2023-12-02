from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment
from datetime import date

def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog_directory.sql")
    repository = PostRepository(db_connection)
    post = repository.find_with_comments(1)
    
    assert post == Post(1, 'Title 1', 'Content 1', comments=[
        Comment(1, 'Comment 1', 'Author 1', 1),
        Comment(2, 'Comment 2', 'Author 2', 1),
    ])