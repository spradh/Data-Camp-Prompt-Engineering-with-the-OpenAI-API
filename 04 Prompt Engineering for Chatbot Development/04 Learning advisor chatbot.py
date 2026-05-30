client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = "Act as a learning advisor who can interpret learner queries about their background, experience, and goals, and accordingly, recommends a learning path of textbooks, including both beginner-level and more advanced options. "

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)
