{{ config(materialized='table') }}

{% set profile_columns = ['age_group', 'job', 'marital', 'education', '`default`', 'housing', 'loan', 'deposit'] %}

WITH bank AS (
  SELECT
    *,
    CASE
      WHEN age < 40 THEN 'young adult'
      WHEN age >= 40 AND age < 60 THEN 'middle-aged adult'
      WHEN age >= 60 THEN 'old adult'
    END AS age_group
  FROM {{ ref('bank')}}
)

SELECT 
  {% for profile_column in profile_columns %}
    {{ profile_column }},
  {% endfor %}
  COUNT(1) AS client_count
FROM 
  bank
GROUP BY
  {% for profile_column in profile_columns %}
    {{ profile_column }}{% if not loop.last %},{% endif %}
  {% endfor %}