DROP TABLE IF EXISTS place;
DROP TABLE IF EXISTS item;

CREATE TABLE place (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    xpos FLOAT,
    ypos FLOAT
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    place_id INTEGER,
    name TEXT,
    desc TEXT,
    xpos FLOAT,
    ypos FLOAT,
    FOREIGN KEY (place_id) REFERENCES place(id)
);

INSERT INTO place (name, xpos, ypos) VALUES
    ('kielce', 20, 50);

INSERT INTO ITEM (place_id, name, desc, xpos, ypos) VALUES
    (1, 'hello1', 'srutututu', 20, 20),
    (1, 'hello2', 'srututtu', 40, 40)
