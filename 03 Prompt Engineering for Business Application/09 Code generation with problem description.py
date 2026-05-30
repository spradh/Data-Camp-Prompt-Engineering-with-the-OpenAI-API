client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = """
Write a Python function that receives a list of 12 floats representing monthly sales data as input and, return the month with the highest sales value as output.
"""

response = get_response(prompt)
print(response)
