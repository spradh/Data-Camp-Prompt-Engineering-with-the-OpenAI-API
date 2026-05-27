client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = """You will be provided with an excerpt delimited by triple backticks. Infer ite's language, generate a title and determine the number of sentences in the excerpt. Only generate a suitable title if there are more than one sentences, else set title to 'N/A'"""

# Create the output format
output_format = """
Use the following format for the output:
- Text: <the text>
- Language: <the lanugage>
- Number of sentences: <the number of sentences in the text>
- Title: <the title>

"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)
