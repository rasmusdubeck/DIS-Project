DROP TABLE IF EXISTS users;


CREATE TABLE users (
    username      TEXT NOT NULL,
    ID SERIAL PRIMARY KEY,
    email         TEXT NOT NULL,
    skill_level   INTEGER NOT NULL,
    postal_code   INTEGER NOT NULL
);

COPY users(username,ID,email,skill_level,postal_code)
FROM '/docker-entrypoint-initdb.d/users.csv'
WITH (FORMAT csv, HEADER true);

SELECT setval(pg_get_serial_sequence('users','id'), (SELECT MAX(id) FROM users) + 1);
