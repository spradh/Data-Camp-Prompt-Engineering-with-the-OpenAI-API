client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f""" Modify the function delimited by triple backticks according to the following specified requirements:
- test if the inputs to the funtions are positive. 
- If the inputs are not positive, display an error message. Otherwise return area and perimeter of the rectangle

Function:
{function}
"""
response = get_response(prompt)
print(response)
