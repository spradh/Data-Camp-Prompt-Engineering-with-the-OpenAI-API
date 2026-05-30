client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""
Explain the following function step by step. 

Function:
```{function}```"""
 
response = get_response(prompt)
print(response)
