client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f""""
Assess the function provided below according to the three criteria: correct syntax, receiving two inputs, and returning one output.

Code:

```{code}```
""" 

response = get_response(prompt)
print(response)
