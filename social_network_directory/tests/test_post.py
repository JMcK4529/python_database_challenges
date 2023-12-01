from lib.post import Post

"""
Post construsts with an id, title, content, views and user_account_id
"""
def test_post_constructs():
    post = Post(1, "Test Title", "Test Content", 700, 3)
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.views == 700
    assert post.user_account_id == 3

"""
Posts are formatted to strings in a readable way
"""
def test_post_to_string():
    post = Post(1, "Test Title", "Test Content", 700, 3)
    assert str(post) == "Post(1, Test Title, Test Content, 700, 3)"

"""
Comparing two instances of Post with the same data should
result in them being equal
"""
def test_post_equality():
    post1 = Post(1, "Test Title", "Test Content", 700, 3)
    post2 = Post(1, "Test Title", "Test Content", 700, 3)
    assert post1 == post2