USE turbo_train;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email, password) VALUES
    ('user1', 'user1@example.com', 'yeet'),
    ('user2', 'user2@example.com', 'zoinks'),
    ('test', 'test@test.test', 'test');
