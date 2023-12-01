from lib.database_connection import DatabaseConnection
from lib.user_account_repository import UserAccountRepository
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/social_network.sql")

# Retrieve all user_accounts
user_account_repository = UserAccountRepository(connection)
user_accounts = user_account_repository.all()

# List them out
print("UserAccountRepository#all():")
for user_account in user_accounts:
    print(f"    {user_account}")

# Retrieve all posts
post_repository = PostRepository(connection)
posts = post_repository.all()

# List posts to terminal
print("\nPostRepository#all():")
for post in posts:
    print(f"    {post}")

# Retrieve post with id = 1
post1 = post_repository.find(1)
print(f"\nPostRepository#find(1): {post1}")