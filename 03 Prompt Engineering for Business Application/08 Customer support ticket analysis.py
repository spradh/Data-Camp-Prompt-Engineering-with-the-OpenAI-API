client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""
Extract key entities from ticket.

Ticket: {ticket_1} -> Entity: {entities_1}
Ticket: {ticket_2} -> Entity: {entities_2}
Ticket: {ticket_3} -> Entity: {entities_3}
Ticket: {ticket_4} -> 

"""

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)
