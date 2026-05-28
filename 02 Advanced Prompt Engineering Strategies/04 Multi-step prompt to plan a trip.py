client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt detailing steps to plan the trip
prompt = """Generate a plan for a beach vacation. Include four potential locations each with some accommodation options, some activities, and an evaluation of the pros and cons. """

response = get_response(prompt)
print(response)
