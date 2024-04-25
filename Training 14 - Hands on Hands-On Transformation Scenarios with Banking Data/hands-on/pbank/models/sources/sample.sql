{{ config(materialized='table')}}

SELECT *
FROM {{ source('dbtLearn', 'raw_bank')}}