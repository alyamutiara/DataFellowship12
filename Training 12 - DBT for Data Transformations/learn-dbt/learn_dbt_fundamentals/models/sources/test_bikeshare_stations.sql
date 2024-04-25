{{ config(materialization='table') }}

SELECT 
    *
FROM
    {{ source('austin_bikeshare', 'bikeshare_stations') }}
LIMIT 1