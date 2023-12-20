DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

DROP TABLE IF EXISTS expenses;
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255) NOT NULL,
    amount INT NOT NULL,
    user_id INT,
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO users (username, name, password) VALUES ('admin', 'Administrator', 'admin');
