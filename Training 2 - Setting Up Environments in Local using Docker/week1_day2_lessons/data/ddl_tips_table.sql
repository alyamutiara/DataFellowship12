CREATE TABLE tips (
    id VARCHAR(20) PRIMARY KEY,
    weekday VARCHAR(20),
    meal_type VARCHAR(20),
    wait_staff VARCHAR(50),
    party_size VARCHAR(20),
    meal_total VARCHAR(20),
    tip VARCHAR(20)
);


COPY tips_table FROM 'gs://testing_bucket_again/data/tips.csv' WITH (FORMAT csv, HEADER true);