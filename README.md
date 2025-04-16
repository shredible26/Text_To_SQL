**Text_To_SQL**

TextToSQL is a command-line tool that uses OpenAI's GPT-3.5-Turbo model to generate dummy CSV data and translate natural language queries into SQL statements. 

Features:

- Dummy Data Generation: The program will prompt the user for a category (Financial, Sports, Healthcare etc)
  along with parameters including number of rows and columns desired. It then calls the OpenAI API to generate dummy CSV data relevant to the selected category.

- Natural Language to SQL Conversion: After generating the data, the program then aks the user for the information they want to extract.
  (e.g. 'I want to find the average amount sales among all customers over 25 years old and then within these customers I want to find those
  that spend in between $5000 and $10000 anually, and then sort them by spending in descending order'.

- It converts the natural language request into a structured SQL query based on the provided data schema and sample dummy data.

Requirements:

- Python 3.7 or higher
- OpenAI Python Library (https://github.com/openai/openai-python)
- pandas for data manipulation
- python-dotenv for managing environment variables

Cloning:
   ```bash
   git clone https://github.com/shredible26/Text_To_SQL.git
   cd Text_To_SQL
