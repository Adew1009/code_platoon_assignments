from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are Rambo at the end of the movie first blood."},  # "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
    {"role": "user", "content": "explain to me me about how the differences between binary search and simple search."} #"Compose a poem that explains the concept of recursion in programming."
  ]
)

print(completion.choices[0].message)