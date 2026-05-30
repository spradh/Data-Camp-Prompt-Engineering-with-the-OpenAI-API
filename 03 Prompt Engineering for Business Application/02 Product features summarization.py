client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = f"""
Summarize the following product description into an easy to read bullet point summary. There should be no more than 5 bullet points.

Product description:
{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)
