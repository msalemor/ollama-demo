from openai import OpenAI
client = OpenAI(base_url='http://localhost:11434/v1',api_key='ollama')

response = client.chat.completions.create(
  model="phi3.5",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "In one sentence, what is the speed of light?"}
  ]
)

print(response.choices[0].message.content)