client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the chain-of-thought prompt
prompt = "Determine your friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20. A: Let's thing about this set by step."

response = get_response(prompt)
print(response)
