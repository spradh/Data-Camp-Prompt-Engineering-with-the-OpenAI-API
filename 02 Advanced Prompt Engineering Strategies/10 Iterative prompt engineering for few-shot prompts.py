client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
The brown cat jump up on the wall -> no explicit emotion
They ran back to the house -> no explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)
