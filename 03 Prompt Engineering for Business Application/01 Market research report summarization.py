client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""
Summarize the following report in five sentences and  focus on aspects related AI and data privacy and how they are affecting customers.

Report:
{report}
"""

response = get_response(prompt)

print("Summarized report: \n", response)
