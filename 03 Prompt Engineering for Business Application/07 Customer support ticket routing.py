client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""
Classify the ticket delimited by backticks as either technical issue, billing inquiry or product feedback.
Ticket:
{ticket}
"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)
