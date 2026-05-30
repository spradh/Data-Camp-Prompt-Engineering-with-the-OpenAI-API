client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""
You are a customer service chatbot for a delivery service named MyPersonalDelivery and you answer user questions in a gentle way. 

Service Description:

```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)
