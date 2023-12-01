from lib.user_account import UserAccount

class UserAccountRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM user_accounts;")
        user_accounts = []
        for row in rows:
            user_account = UserAccount(row["id"], row["email"], row["username"])
            user_accounts.append(user_account)
        return user_accounts

    def find(self, user_account_id):
        row = self._connection.execute(
            "SELECT * FROM user_accounts WHERE id = %s;",
              [user_account_id]
              )[0]
        return UserAccount(row["id"], row["email"], row["username"]) 

    def create(self, user_account):
        self._connection.execute(
            "INSERT INTO user_accounts (email, username)" +
            " VALUES (%s, %s);", 
            [user_account.email, user_account.username]
            )
        return None

    def delete(self, user_account_id):
        self._connection.execute(
            "DELETE FROM user_accounts WHERE id = %s;",
            [user_account_id]
        )
        return None