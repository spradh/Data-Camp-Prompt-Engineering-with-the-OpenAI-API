client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = "Give me the top 10 pre-trained language models, Organize the results in a table with 3 columns for model name, release year and owning company."

response = get_response(prompt)
print(response)
