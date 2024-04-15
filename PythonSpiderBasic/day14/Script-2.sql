CREATE TABLE men (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
    address VARCHAR(255)
);
INSERT INTO men (name, age, address) VALUES
    ('John Doe', 30, '123 Main St'),
    ('Alice Smith', 25, '456 Elm Ave'),
    ('Michael Johnson', 40, '789 Oak Rd'),
    ('Emily Brown', 22, '567 Pine Ln'),
    ('David Lee', 28, '321 Maple Dr'),
    ('Sophia Garcia', 35, '987 Birch Ct'),
    ('Daniel White', 33, '654 Cedar Rd'),
    ('Olivia Martinez', 29, '890 Walnut Ave'),
    ('William Taylor', 27, '234 Spruce Ln'),
    ('Emma Harris', 31, '432 Cherry St');
