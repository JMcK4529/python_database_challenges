-- file: social_network.sql

DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS user_accounts;

-- Create the table without the foreign key first.
CREATE TABLE user_accounts (
  id SERIAL PRIMARY KEY,
  email text,
  username text
);

-- Then the table with the foreign key second.
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
  views int,
-- The foreign key name is always {other_table_singular}_id
  user_account_id int,
  constraint fk_user_account foreign key(user_account_id)
    references user_accounts(id)
    on delete cascade
);

INSERT INTO user_accounts (email, username) VALUES ('user1@address.com', 'username1');
INSERT INTO user_accounts (email, username) VALUES ('user2@address.com', 'username2');
INSERT INTO user_accounts (email, username) VALUES ('user3@address.com', 'username3');
INSERT INTO user_accounts (email, username) VALUES ('user4@address.com', 'username4');

INSERT INTO posts (title, content, views, user_account_id) VALUES ('User1 Post1', 'I feel sad', 3, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User1 Post2', 'My hotel room is dirty :(', 17, 1);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User2 Post1', 'I feel happy', 58, 2);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User2 Post2', 'My partner proposed!', 201, 2);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User3 Post1', 'I feel like my account has no views', 0, 3);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User3 Post2', 'Can anybody see this?', 0, 3);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User4 Post1', 'I feel hungry', 10, 4);
INSERT INTO posts (title, content, views, user_account_id) VALUES ('User4 Post2', 'Time to go to lunch', 1, 4);