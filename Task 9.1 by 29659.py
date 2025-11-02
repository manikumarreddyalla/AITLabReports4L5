import openai

openai.api_key = "YOUR_API_KEY_HERE"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user",
"content": "Give me 3 ideas that i could build using openai apis"}])
print(completion.choices[0].message.content)
