# %% [markdown]
# # graeat expectations 101
# 
# [getting started for Great Expectations](https://www.youtube.com/watch?v=uM9DB2ca8T8&t=1216s&ab_channel=GreatExpectations)

# %%
import great_expectations as gx
import pandas as pd

# %%
# create data context
context = gx.get_context()

# %%
df = pd.read_csv("/Users/moca/PycharmProjects/pythonProject/data/yellow_tripdata_sample_2019.csv")

# %%
df.head()

# %%
df.count()

# %%
print(df.columns)
print(len(df.columns))

# %%
# read data from local machine using gx function
validator = context.sources.pandas_default.read_csv(
    "/Users/moca/PycharmProjects/pythonProject/data/yellow_tripdata_sample_2019.csv"
)

# %%
type(validator)

# %%
# if you prefer using the pandas dataframe above you can use this
#validator = gx.from_pandas(df)

# %%
print(df.count)

# %%
validator.expect_column_values_to_not_be_null("pickup_datetime")
validator.expect_column_values_to_be_between(
    "passenger_count", min_value=1, max_value=6
)
validator.expect_table_column_count_to_equal(18)
validator.save_expectation_suite()

# %%
validator.save_expectation_suite()

# %%
# check the uninque ness of a column
df.trip_distance.unique()

# %%


# %%
# special charracter not tobe expected exist at this dataframe

validator.expect_column_values_to_match_regex() 


