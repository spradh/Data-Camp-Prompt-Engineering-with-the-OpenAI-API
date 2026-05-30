client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to expand the product's description
prompt = f"""
Generate a detailed one paragraph product description that provides a comprehensive overview that captures key information of the product, specifically its unique features, benefits and potential applications.

Below is a short description of the product:
{product_description}


"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)
