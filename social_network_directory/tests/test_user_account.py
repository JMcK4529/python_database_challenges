from lib.user_account import UserAccount

"""
UserAccount construsts with an id, email, username
"""
def test_user_account_constructs():
    user_account = UserAccount(1, "TestEmail@Address.com", "TestUsername")
    assert user_account.id == 1
    assert user_account.email == "TestEmail@Address.com"
    assert user_account.username == "TestUsername"

"""
UserAccounts are formatted to strings in a readable way
"""
def test_user_account_to_string():
    user_account = UserAccount(1, "TestEmail@Address.com", "TestUsername")
    assert str(user_account) == "UserAccount(1, TestEmail@Address.com, TestUsername)"

"""
Comparing two instances of UserAccount with the same data should
result in them being equal
"""
def test_user_account_equality():
    user_account1 = UserAccount(1, "TestEmail@Address.com", "TestUsername")
    user_account2 = UserAccount(1, "TestEmail@Address.com", "TestUsername")
    assert user_account1 == user_account2