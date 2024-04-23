CREATE TABLE suicides_data (
  country VARCHAR(255) NOT NULL,
  year  NOT NULL,
  sex VARCHAR(255) NOT NULL,
  age VARCHAR(255) NOT NULL,
  suicides_no INTEGER NOT NULL,
  population INTEGER NOT NULL,
  "suicides/100k pop" DECIMAL(10,2) NOT NULL,  -- Double quotes around column name for clarity
  "country-year" VARCHAR(255) NOT NULL,  -- Double quotes around column name for clarity
  "HDI for year" VARCHAR(255),  -- Might be numeric depending on actual data
  "gdp_for_year ($)" VARCHAR(255),  -- Might be numeric depending on actual data
  "gdp_per_capita ($)" INTEGER,  -- Adjust if you have actual numeric values
  generation VARCHAR(255) NOT NULL
);