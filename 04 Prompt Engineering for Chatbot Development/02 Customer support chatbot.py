client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the purpose of the chatbot
chatbot_purpose = "You are a customer support chatbot for an e-commerce company specializing in electronics. You will assist users with inquiries, order tracking, and troubleshooting common issues."

# Define audience guidelines
audience_guidelines = "Your target audience is a tech-savy individual interested in purchasing electronic gadgets."

# Define tone guidelines
tone_guidelines = "Use a professional and user-friendly tone while interacting with customers."

system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(system_prompt, "My new headphones aren't connecting to my device")
print(response)
