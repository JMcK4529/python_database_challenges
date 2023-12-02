from lib.comment import Comment

def test_comment_constructs():
    id, comment_content, author_name, post_id = \
                                        1, "Test Content", "Johnny Test", 1
    comment = Comment(id, comment_content, author_name, post_id)
    for attribute in zip([comment.id, comment.comment_content,
                          comment.author_name, comment.post_id],
                         [id, comment_content, author_name, post_id]):
        assert attribute[0] == attribute[1]

def test_comment_repr_magic_method():
    id, comment_content, author_name, post_id = \
                                        1, "Test Content", "Johnny Test", 1
    comment = Comment(id, comment_content, author_name, post_id)
    assert str(comment) == "Comment(1, Test Content, Johnny Test, 1)"

def test_comment_eq_magic_method():
    id, comment_content, author_name, post_id = \
                                        1, "Test Content", "Johnny Test", 1
    comment1 = Comment(id, comment_content, author_name, post_id)
    comment2 = Comment(id, comment_content, author_name, post_id)
    assert comment1 == comment2