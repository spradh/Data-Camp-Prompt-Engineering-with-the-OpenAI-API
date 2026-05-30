client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that translates
prompt = f"""
Translate the product description and marketing from English to French, Spanish and Japanese:

{marketing_message}
"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)
