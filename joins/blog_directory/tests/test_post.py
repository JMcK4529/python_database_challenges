from lib.post import Post
from unittest.mock import MagicMock

def test_post_constructs():
    comments_mock = [MagicMock() for _ in range(3)]
    for comment_mock in comments_mock:
        comment_mock.__eq__.return_value = True

    id, title, post_content, comments = (1, "Test Cohort",
                                         "2023-12-01", comments_mock)
    
    post = Post(id, title, post_content, comments_mock)
    for attribute in zip([post.id, post.title,
                          post.post_content, post.comments],
                         [id, title, post_content, comments]):
        assert attribute[0] == attribute[1]

def test_post_repr_magic_method():
    comments_mock = [MagicMock() for _ in range(3)]
    for comment_mock in comments_mock:
        comment_mock.__eq__.return_value = True

    id, title, post_content, comments = (1, "Test Cohort",
                                         "2023-12-01", comments_mock)
    
    post = Post(id, title, post_content)
    assert str(post) == "Post(1, Test Cohort, 2023-12-01, comments=[])"

def test_post_eq_magic_method():
    comments_mock = [MagicMock() for _ in range(3)]
    for comment_mock in comments_mock:
        comment_mock.__eq__.return_value = True
    
    id, title, post_content, comments = (1, "Test Cohort",
                                         "2023-12-01", comments_mock)
    post1 = Post(id, title, post_content, comments)
    post2 = Post(id, title, post_content, comments)
    assert post1 == post2