CREATE TABLE IF NOT EXISTS jobs(
    id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(250) NOT NULL,
    location VARCHAR(250) NOT NULL,
    salary INT,
    currency VARCHAR(10),
    responsibilities VARCHAR(2000),
    requirements VARCHAR(2000),
    PRIMARY KEY (id)
)