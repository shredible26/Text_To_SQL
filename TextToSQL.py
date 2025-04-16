import os
from dotenv import load_dotenv

# Load environment variables from keys.env BEFORE using them
load_dotenv('keys.env')

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import pandas as pd
import json
from io import StringIO

# Asks the user for a category to generate dummy data.
category = input("Enter a category for dummy data (e.g., Financial, Sports, Healthcare, etc). You may specify how large (rows and columns) the dummy data should be:")

# Generate dummy data using OpenAI (GPT-4).
prompt_dummy = f"""
You are an expert data generator. Given the category "{category}", generate dummy data in CSV format including a header.
The CSV should include a minimum of 5 columns and 5 rows relevant to this category. If the user provides specifics for the number of rows or columns or the size of the dummy data, build the data accordingly.
Only output the CSV data and nothing else.
"""

response_dummy = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You generate dummy data in CSV format for a given category."},
        {"role": "user", "content": prompt_dummy}
    ],
    temperature=0.7
)
dummy_csv = response_dummy.choices[0].message.content.strip()

print("\n Dummy Data CSV")
print(dummy_csv)

# Use StringIO to load CSV data and pandas to access the file
data = pd.read_csv(StringIO(dummy_csv))
print("\n Dummy Data as DataFrame")
print(data)

# Asks user what analysis/information to extract.
user_question = input("\nWhat information or correlations would you like to extract from this data?")

# Generates a SQL query based on the user's natural language request.
prompt_sql = f"""
You are an expert in SQL. The table 'dummy_table' has the following structure and sample data:

Columns and Data Types:
{data.dtypes.to_string()}

Sample Data:
{data.head().to_string(index=False)}

Based on the user request below, please generate a SQL query that extracts the desired information or correlations based on the user's request.
User request: "{user_question}"

Make sure the output is solely a SQL query.
"""

response_sql = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You translate natural language into SQL queries based on a table's schema and data sample."},
        {"role": "user", "content": prompt_sql}
    ],
    temperature=0
)
sql_query = response_sql.choices[0].message.content.strip()
print("\n Generated SQL Query:")
print(sql_query)