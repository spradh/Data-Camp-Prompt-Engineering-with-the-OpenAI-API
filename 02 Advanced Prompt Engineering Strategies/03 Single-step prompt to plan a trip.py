client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a single-step prompt to get help planning the vacation
prompt = "Generate a itinerary for a beach vacation."

response = get_response(prompt)
print(response)
