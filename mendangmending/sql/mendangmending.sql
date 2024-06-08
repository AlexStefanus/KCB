-- mendangmending.sql
CREATE DATABASE mendangmending;
USE mendangmending;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    score INT NOT NULL,
    image VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    pros TEXT NOT NULL,
    cons TEXT NOT NULL
);