client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "Ask for order number if not already provided."

# Define the technical issue condition
technical_issue_condition = "If the user is asking about a technical issue, start your respond with, 'I'm sorry to hear about your issue ...'"

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)
