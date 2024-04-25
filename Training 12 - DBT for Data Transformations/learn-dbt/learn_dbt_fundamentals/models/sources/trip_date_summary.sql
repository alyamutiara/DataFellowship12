WITH trip_date_summary AS (
    SELECT
        DATE(start_time) AS trip_date,
        SUM(duration_minutes) AS total_trip_duration
    FROM
        {{ source('austin_bikeshare', 'bikeshare_trips')}}
    GROUP BY
        DATE(start_time)
), trip_date_summary_with_prev AS (
    SELECT
        *,
        LAG(total_trip_duration) OVER (ORDER BY trip_date ASC) AS prev_total_trip_duration
    FROM
        trip_date_summary
)

SELECT
    trip_date,
    total_trip_duration AS current_total,
    prev_total_trip_duration As prev_total,
    total_trip_duration - prev_total_trip_duration AS delta_total
FROM
    trip_date_summary_with_prev
ORDER BY trip_date ASC