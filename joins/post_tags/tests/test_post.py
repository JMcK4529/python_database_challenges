from lib.post import Post

def test_post_init():
    post = Post('1', 'Title 1')
    assert post.id == '1'
    assert post.title == 'Title 1'
    assert post.tags == []

def test_post_repr():
    assert str(Post('1', 'Title 1')) == \
        "Post(1, Title 1, tags=[])"

def test_post_eq():
    post1 = Post('1', 'Title 1')
    post2 = Post('1', 'Title 1')
    assert post1 == post2