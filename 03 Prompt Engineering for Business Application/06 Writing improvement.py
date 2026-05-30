client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to transform the text
prompt = f"""
Proofread the following text adn adjust tone to be formal and friendly.

Text:
{text}
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)
