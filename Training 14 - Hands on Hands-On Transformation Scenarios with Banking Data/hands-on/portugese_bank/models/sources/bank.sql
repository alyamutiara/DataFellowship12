{{ config(materialized='table') }}

SELECT
    * EXCEPT (
        `default`,
        housing,
        loan,
        `month`,
        deposit
    ),
    `default` = 'yes' AS `default`,
    housing = 'yes' AS housing,
    loan = 'yes' AS loan,
    EXTRACT(MONTH FROM PARSE_DATE('%b', `month`)) AS `month`,
    deposit = 'yes' AS deposit
FROM
    {{ source('dbtLearn', 'raw_bank') }}