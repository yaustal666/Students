create table IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	username TEXT,
  	email TEXT,
  	age INTEGER
);

DROP TABLE users;


INSERT INTO users (username, email, age) VALUES ('jane_smith', 'jane@email.com', 32);
INSERT INTO users (username, email, age) VALUES ('bob_wilson', 'bob@email.com', 19);
INSERT INTO users (username, email, age) VALUES ('alice_brown', 'alice@email.com', 28);
INSERT INTO users (username, email, age) VALUES ('charlie_davis', 'charlie@email.com', 45);

SELECT * from users
WHERE age > 21
ORDER BY age DESC;

SELECT * FROM users
WHERE id = 5;

UPDATE users
SET username = 'lol'
WHERE id = 5;

DELETE FROM users
WHERE id = 5;