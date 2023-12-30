from lib.post_repository import PostRepository
from lib.post import Post
from unittest.mock import Mock

def test_post_repo_init():
    try:
        connection = Mock()
        repo = PostRepository(connection)
        assert repo != None
    except Exception as err:
        raise AssertionError("An error was raised during instantiation:" +
                             f"\n{err}")

def test_post_repo_all(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepository(db_connection)
    assert repo.all() == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]

def test_post_repo_find_by_id(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepository(db_connection)
    posts = [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(4, 'My weekend in Edinburgh'),
        Post(5, 'The best chocolate cake EVER'),
        Post(6, 'A foodie week in Spain'),
        Post(7, 'SQL basics')
    ]
    for id, index in zip(range(1,8), range(7)):
        found = repo.find_by_id(id)
        assert found == posts[index]

def test_post_repo_find_by_tag(db_connection):
    db_connection.seed("seeds/blog_posts_tags.sql")
    repo = PostRepository(db_connection)
    assert repo.find_by_tag('coding') == [
        Post(1, 'How to use Git'),
        Post(2, 'Fun classes'),
        Post(3, 'Using a REPL'),
        Post(7, 'SQL basics')
    ]