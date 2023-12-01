from lib.post_repository import PostRepository
from lib.post import Post

"""
PostRepository.all returns all the posts (and all columns) from
the database
"""
def test_all_records_retrieved_by_all_method(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, "User1 Post1", "I feel sad", 3, 1),
        Post(2, "User1 Post2", "My hotel room is dirty :(", 17, 1),
        Post(3, "User2 Post1", "I feel happy", 58, 2),
        Post(4, "User2 Post2", "My partner proposed!", 201, 2),
        Post(5, "User3 Post1", "I feel like my account has no views", 0, 3),
        Post(6, "User3 Post2", "Can anybody see this?", 0, 3),
        Post(7, "User4 Post1", "I feel hungry", 10, 4),
        Post(8, "User4 Post2", "Time to go to lunch", 1, 4),
    ]

"""
PostRepository.find(n) returns the Post whose id == n
"""
def test_single_record_with_correct_id_retrieved_by_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = repository.find(6)
    assert post == Post(6, "User3 Post2", "Can anybody see this?", 0, 3)


"""
PostRepository.create(post)
inserts a post into posts table
"""
def test_single_post_created_with_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    new_post = Post(None, "title", "content", 0, 4)
    repository.create(new_post)
    assert repository.find(9) == Post(9, "title", "content", 0, 4)
    assert repository.all() == [
        Post(1, "User1 Post1", "I feel sad", 3, 1),
        Post(2, "User1 Post2", "My hotel room is dirty :(", 17, 1),
        Post(3, "User2 Post1", "I feel happy", 58, 2),
        Post(4, "User2 Post2", "My partner proposed!", 201, 2),
        Post(5, "User3 Post1", "I feel like my account has no views", 0, 3),
        Post(6, "User3 Post2", "Can anybody see this?", 0, 3),
        Post(7, "User4 Post1", "I feel hungry", 10, 4),
        Post(8, "User4 Post2", "Time to go to lunch", 1, 4),
        Post(9, "title", "content", 0, 4)
    ]

"""
PostRepository.delete(post_id) deletes
the post associated with id = post_id
"""
def test_single_post_deleted_with_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    old_post = Post(4, "User2 Post2", "My partner proposed!", 201, 2)
    repository.delete(old_post.id)
    assert old_post not in repository.all()
    assert repository.all() == [
        Post(1, "User1 Post1", "I feel sad", 3, 1),
        Post(2, "User1 Post2", "My hotel room is dirty :(", 17, 1),
        Post(3, "User2 Post1", "I feel happy", 58, 2),
        Post(5, "User3 Post1", "I feel like my account has no views", 0, 3),
        Post(6, "User3 Post2", "Can anybody see this?", 0, 3),
        Post(7, "User4 Post1", "I feel hungry", 10, 4),
        Post(8, "User4 Post2", "Time to go to lunch", 1, 4)
    ]