client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = """Generate a table of 10 books with columns for Title, Author and Year that you would recommend to a science fiction lover."""

# Get the response
response = get_response(prompt)
print(response)
