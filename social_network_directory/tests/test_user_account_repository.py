from lib.user_account_repository import UserAccountRepository
from lib.user_account import UserAccount

"""
PostRepository.all returns all the user_accounts (and all columns) from
the database
"""
def test_all_records_retrieved_by_all_method(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)

    user_accounts = repository.all()

    assert user_accounts == [
        UserAccount(1, 'user1@address.com', 'username1'),
        UserAccount(2, 'user2@address.com', 'username2'),
        UserAccount(3, 'user3@address.com', 'username3'),
        UserAccount(4, 'user4@address.com', 'username4')
    ]

"""
UserAccountRepository.find(n) returns the UserAccount whose id == n
"""
def test_single_record_with_correct_id_retrieved_by_find(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    user_account = repository.find(3)
    assert user_account == UserAccount(3, 'user3@address.com', 'username3')

"""
UserAccountRepository.create(user_account)
inserts an account into user_accounts table
"""
def test_single_user_account_created_with_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    new_user_account = UserAccount(None, 'testuser@fakeaddress.com',
                                    'testusername')
    repository.create(new_user_account)
    assert repository.find(5) == UserAccount(5, 'testuser@fakeaddress.com',
                                              'testusername')
    assert repository.all() == [
        UserAccount(1, 'user1@address.com', 'username1'),
        UserAccount(2, 'user2@address.com', 'username2'),
        UserAccount(3, 'user3@address.com', 'username3'),
        UserAccount(4, 'user4@address.com', 'username4'),
        UserAccount(5, 'testuser@fakeaddress.com', 'testusername')
    ]

"""
UserAccountRepository.delete(user_account_id) deletes
the account associated with id = user_acount_id
"""
def test_single_user_account_deleted_with_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserAccountRepository(db_connection)
    old_user_account = UserAccount(3, 'user3@address.com', 'username3')
    repository.delete(old_user_account.id)
    assert old_user_account not in repository.all()
    assert repository.all() == [
        UserAccount(1, 'user1@address.com', 'username1'),
        UserAccount(2, 'user2@address.com', 'username2'),
        UserAccount(4, 'user4@address.com', 'username4')
    ]