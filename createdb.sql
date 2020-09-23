CREATE TABLE Users(
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(40)
);

CREATE TABLE WeeklyAffairs(
    user_id INTEGER REFERENCE Users(user_id),
    day INT,
    time INT,
    data TEXT
);

CREATE TABLE Affairs(
    user_id INTEGER REFERENCE Users(user_id),
    date INT,
    time INT,
    data TEXT
);
