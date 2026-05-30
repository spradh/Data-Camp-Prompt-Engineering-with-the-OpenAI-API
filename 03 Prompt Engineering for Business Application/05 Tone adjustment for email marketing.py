client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to change the email's tone
prompt = f"""
Craft the following email in a professional, positive and user-centric tone.

Email:
{sample_email}
"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)
