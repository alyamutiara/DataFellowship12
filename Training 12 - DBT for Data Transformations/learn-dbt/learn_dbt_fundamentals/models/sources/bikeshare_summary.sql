{{ config(materialization='view') }}

SELECT
    bike_id,
    SUM(duration_minutes) AS total_minutes_used,
    COUNT(1) AS total_trips
FROM
    {{ source('austin_bikeshare', 'bikeshare_trips')}}
WHERE
    bike_type = 'electric'
GROUP BY
    bike_id
ORDER BY total_minutes_used DESC, total_trips DESC