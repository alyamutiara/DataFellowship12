DROP TABLE IF EXISTS "customers";

CREATE TABLE customers (
    step INT,
    customer VARCHAR(255),
    age INT,
    gender VARCHAR(1),
    zipcodeOri VARCHAR(7),
    merchant VARCHAR(255),
    zipMerchant INT,
    category VARCHAR(255),
    amount NUMERIC,
    fraud BOOLEAN
);

GRANT READ ON '/customers_data.csv' TO banksim;

COPY customers (
    step, customer, age, gender, zipcodeOri, merchant, zipMerchant, category, amount, fraud
) 
FROM '/customers_data.csv' DELIMITER ',' CSV HEADER;

DROP TABLE IF EXISTS "transactions";
CREATE TABLE transactions (
    source VARCHAR(255),
    target VARCHAR(255),
    weight NUMERIC,
    typeTrans VARCHAR(255),
    fraud BOOLEAN
);

GRANT READ ON '/transactions_data.csv' TO banksim;

COPY transactions (
    source, target, weight, typeTrans, fraud
)
FROM '/transactions_data.csv' DELIMITER ',' CSV HEADER;