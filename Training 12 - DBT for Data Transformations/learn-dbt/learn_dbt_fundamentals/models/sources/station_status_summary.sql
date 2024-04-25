{{ config(materialization='view') }}

SELECT
    status,
    COUNT(1) AS total_stations
FROM
    {{ source('austin_bikeshare', 'bikeshare_stations')}}
GROUP BY status
ORDER BY total_stations DESC